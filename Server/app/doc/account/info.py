from app.doc import JWT_ACCESS_TOKEN

EXTENSION_INFO_GET = {
    'tags': ['Info'],
    'description': '학생 자신의 신청 정보를 조회합니다.',
    'parameters': [JWT_ACCESS_TOKEN],
    'responses': {
        '200': {
            'description': '신청 정보 조회 성공',
            'examples': {
                '': {
                    'extension11': {
                        'classNum': 2,
                        'seatNum': 13
                    },
                    'extension12': None,
                    'goingOut': [
                        {
                            'goOutDate': '2019-01-01 8:00',
                            'returnDate': '2019-01-01 9:00',
                            'reason': '아침 식사 외출(서브웨이)'
                        },
                        {
                            'goOutDate': '2019-01-01 12:00',
                            'returnDate': '2019-01-01 13:00',
                            'reason': '점심 식사 외출(베스타)'
                        },
                        {
                            'goOutDate': '2019-01-01 18:00',
                            'returnDate': '2019-01-01 19:00',
                            'reason': '저녁 식사 외출(신라호텔)'
                        }
                    ],
                    'stay': 4
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}


BASIC_INFO_GET = {
    'tags': ['Info'],
    'description': '학생 자신의 기본 정보(이름, 학번, 상벌점)를 조회합니다.',
    'parameters': [JWT_ACCESS_TOKEN],
    'responses': {
        '200': {
            'description': '마이페이지 조회 성공',
            'examples': {
                '': {
                    'name': '조민규',
                    'number': 20120,
                    'goodPoint': 1,
                    'badPoint': 458756945,
                    'penaltyLevel': 2,
                    'penaltyStatus': True
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POINT_HISTORY_GET = {
    'tags': ['Info'],
    'description': '학생 자신의 상벌점 기록을 조회합니다.',
    'parameters': [JWT_ACCESS_TOKEN],
    'responses': {
        '200': {
            'description': '내역 조회 성공',
            'examples': {
                '': {
                    'point_history': [
                        {
                            'date': '2017-12-17',
                            'reason': '치킨 먹음',
                            'pointType': False,
                            'point': 3
                        },
                        {
                            'date': '2017-12-19',
                            'reason': '치킨 맛있음',
                            'pointType': True,
                            'point': 2
                        }
                    ]
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
