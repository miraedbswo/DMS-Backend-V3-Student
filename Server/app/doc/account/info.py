from app.doc import JWT_ACCESS_TOKEN

EXTENSION_INFO_GET = {
    'tags': ['Account'],
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
                    'goingout': {
                        'sat': True,
                        'sun': False
                    },
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
    'tags': ['Account'],
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
                    'badPoint': 458756945
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

POINT_HISTORY_GET = {
    'tags': ['Account'],
    'description': '학생 자신의 상벌점 기록을 조회합니다.',
    'parameters': [JWT_ACCESS_TOKEN],
    'responses': {
        '200': {
            'description': '내역 조회 성공',
            'examples': {
                '': [
                    {
                        'time': '2017-12-17',
                        'reason': '치킨 먹음',
                        'pointType': False,
                        'point': 3
                    },
                    {
                        'time': '2017-12-19',
                        'reason': '치킨 맛있음',
                        'pointType': True,
                        'point': 2
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
