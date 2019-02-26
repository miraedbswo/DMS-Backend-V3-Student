import requests
from bs4 import BeautifulSoup

url_base = 'https://stu.dje.go.kr/sts_sci_md00_001.do?schulCode=G100000170&schulCrseScCode=4&schulKndScScore=04&schYm={}{:0>2}'


class Meal:
    def __init__(self, date: str, type: str, memu: str):
        self.date = date
        self.type = type
        self.menu = memu


def parse(year: int, month: int):
    # TODO: MealParser
    url = url_base.format(year, month)
    rv: requests.Response = requests.get(url)
    soup = BeautifulSoup(rv.text)
