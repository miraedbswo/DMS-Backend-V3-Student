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
                            'date': '02-27 12:30 ~ 17:30',
                            'id': 'test',
                            'reason': '식사 하러',
                            'goingoutStatus': '외출 전'
                        }
                    ],
                    'saturday': [
                        {
                            'date': '03-01 12:30 ~ 17:30',
                            'id': 'test',
                            'reason': '쇼핑 하러',
                            'goingoutStatus': '외출 중'
                        }
                    ],
                    'sunday': [
                        {
                            'date': '11-22 12:30 ~ 17:30',
                            'id': 'test',
                            'reason': '영화 보러',
                            'goingoutStatus': '복귀'
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
        parameter('date', '외출 나가는 시각 ~ 귀사 시각 (MM-DD HH:MM ~ HH:MM'),
        parameter('reason', '외출 사유')
    ],
    'responses': {
        '201': {
            'description': '외출신청 성공'
        },
        '403': {
            'description': '권한 없음'
        },
        '409': {
            'description': '외출신청 실패(신청 가능 시간 아님)'
        }
    }
}

GOINGOUT_PATCH = {
    'tags': ['Apply'],
    'description': '''외출신청 수정
    
    수정 가능 시간: 월요일 00:00 - 금요일 22:00, 외출 당일날 외출수정은 불가능
    ''',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('applyId', '외출신청 아이디', type_='int'),
        parameter('date', '외출 나가는 시각 ~ 귀사 시각 (MM-DD HH:MM ~ HH:MM'),
        parameter('reason', '외출 사유')
    ],
    'responses': {
        '201': {
            'description': '외출신청 수정 성공'
        },
        '204': {
            'description': '외출신청 수정 실패(수정 가능 시간 아님)'
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
