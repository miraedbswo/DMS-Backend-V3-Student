from app.doc import parameter

MEAL_GET = {
    'tags': ['Meal'],
    'description': '급식 조회',
    'parameters': [
        parameter('day', '조회할 날짜(2019-04-20)', in_='url')
    ],
    'responses': {
        '200': {
            'description': '급식 정보 조회 성공',
            'examples': {
                '': {
                    'breakfast': [
                            '밥',
                            '국',
                            '김치',
                            '반찬1',
                            '반찬2'
                    ],
                    'lunch': [
                            '밥',
                            '국',
                            '김치',
                            '반찬1',
                            '반찬2'
                    ],
                    'dinner': [
                            '밥',
                            '국',
                            '김치',
                            '반찬1',
                            '반찬2'
                    ]
                }
            }
        },
        '205': {
            'description': '잘못된 날짜'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}