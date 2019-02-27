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
                    'workday': [
                        {
                            'go_out_date': '2019-02-27 12:30',
                            'id': 'test',
                            'return_date': '2019-02-27 17:30',
                            'reason': '밥'
                        }
                    ],
                    'saturday': [
                        {
                            'go_out_date': '2019-03-02 12:30',
                            'id': 'test',
                            'return_date': '2019-03-02 17:30',
                            'reason': '쇼핑'
                        }

                    ],
                    'sunday': [
                        {
                            'go_out_date': '2019-03-03 12:30',
                            'id': 'test',
                            'return_date': '2019-03-03 17:30',
                            'reason': '개학 ㅠㅠ'
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
