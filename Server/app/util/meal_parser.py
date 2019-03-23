import re
import ssl

import psycopg2
from datetime import datetime, timedelta
from urllib.request import urlopen
from bs4 import BeautifulSoup

_url_base = \
    'https://stu.dje.go.kr/sts_sci_md00_001.do?schulCode=G100000170&schulCrseScCode=4&schulKndScScore=04&schYm={}{:0>2}'

database = {
    'host': 'ec2.istruly.sexy',
    'dbname': 'dms-test',
    'user': 'postgres',
    'password': 'root'
}

conn = psycopg2.connect(**database)
cursor = conn.cursor()

meal_type = ['조식', '중식', '석식']

now: datetime = datetime.utcnow() + timedelta(hours=9)


class Meal:
    def __init__(self, date: datetime, type: int, meal: str):
        self.date = date
        self.type = type
        self.meal = meal

    def insert_into_database(self):
        cursor.execute(
            'INSERT INTO meal (date, type, meal) VALUES(%s, %s, %s)',
            (self.date, self.type, self.meal)
        )
        del self


def insert_one_day_menus(meal_list_filtered_with_regex: list, year: int, month: int, day: int):
    counter = 0
    menu = ''

    dict_ = {
        'date': datetime(year, month, day),
        'type': None,
        'meal': ''
    }

    for meal in meal_list_filtered_with_regex:
        if re.match('[조중석]식', meal):
            counter += 1

        if counter == 2:
            dict_['type'] = meal_type.index(menu[2:4])
            dict_['meal'] = menu[6:]

            Meal(**dict_).insert_into_database()

            menu = ''
            counter -= 1

        if meal[0] == '/':
            menu = menu + '||' + meal[1:]
        else:
            menu = menu + '||' + meal
    else:
        if not meal_list_filtered_with_regex:
            for i in range(3):
                dict_['type'] = i
                Meal(**dict_).insert_into_database()
        else:
            dict_['type'] = meal_type.index(menu[2:4])
            dict_['meal'] = menu[6:]

        Meal(**dict_).insert_into_database()


def insert_meal_into_database_with_crawling(year: int, month: int):
    url = _url_base.format(year, month)

    context = ssl._create_unverified_context()
    resp = urlopen(url, context=context)
    soup = BeautifulSoup(resp, 'html.parser')

    non_exist_day = -1

    for day_count, today_menus in enumerate([td.text for td in soup.find_all('td') if td.text != ' ']):
        if not today_menus:
            non_exist_day += 1
            continue

        # 빈 td를 날짜로 계산하지 않게 하기 위해서 빈 td의 개수만큼 빼줌
        day = day_count - non_exist_day
        meal_list_filtered_with_regex = re.findall('\[?(\/?[가-힣]+(?:\([가-힣]*\))*)(?:\*|[0-9]|\.)*\]?', today_menus)

        insert_one_day_menus(meal_list_filtered_with_regex, year, month, day)

    conn.commit()


insert_meal_into_database_with_crawling(2019, 3)

conn.close()
cursor.close()
