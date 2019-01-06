from app.doc import JWT_ACCESS_TOKEN, parameter

GOINGOUT_GET = {
    'tags': ['Apply'],
    'description': '학생 자신의 외출신청 정보를 조회합니다.',
    'parameters': [
        JWT_ACCESS_TOKEN
    ],
    'responses': {
        '200': {
            'description': '외출신청 정보 조회 성공',
            'examples': {
                '': {
                    'goingOut': [
                        {
                            'id': 123,
                            'goOutDate': '2019-01-01 8:00',
                            'returnDate': '2019-01-01 9:00',
                            'reason': '아침 식사 외출(서브웨이)'
                        },
                        {
                            'id': 124,
                            'goOutDate': '2019-01-01 12:00',
                            'returnDate': '2019-01-01 13:00',
                            'reason': '점심 식사 외출(베스타)'
                        },
                        {
                            'id': 222,
                            'goOutDate': '2019-01-01 18:00',
                            'returnDate': '2019-01-01 19:00',
                            'reason': '저녁 식사 외출(신라호텔)'
                        }
                    ]
                }
            }
        },
        '204': {
            'description': '외출신청 정보 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

GOINGOUT_POST = {
    'tags': ['Apply'],
    'description': '''외출신청
    
    신청 가능 시간: 월요일 00:00 - 금요일 22:00
    금요귀가, 토요귀가 시 외출 신청이 불가능합니다.
    ''',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('goOutDate', '외출 나가는 시각 (YYYY-MM-DD HH:MM)'),
        parameter('returnDate', '귀사 시각 (YYYY-MM-DD HH:MM)'),
        parameter('reason', '외출 사유')
    ],
    'responses': {
        '201': {
            'description': '외출신청 성공'
        },
        '204': {
            'description': '외출신청 실패(신청 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

GOINGOUT_DELETE = {
    'tags': ['Apply'],
    'description': '외출신청 취소',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('applyId', '외출신청 아이디', type_='int')
    ],
    'responses': {
        '200': {
            'description': '취소 성공'
        },
        '204': {
            'description': '외출신청 없음'
        }
    }
}
