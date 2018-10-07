from app.docs import JWT_ACCESS_TOKEN

STAY_GET = {
    'tags': ['Apply Stay'],
    'description': '학생 자신의 잔류신청 정보를 조회합니다.',
    'parameters': [JWT_ACCESS_TOKEN],
    'responses': {
        '200': {
            'description': '잔류신청 정보 조회 성공',
            'examples': {
                '': {
                    'value': 4
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

STAY_POST = {
    'tags': ['Apply Stay'],
    'description': '''잔류신청
    
    신청 가능 시간: 일요일 20:30 - 목요일 22:00
    ''',
    'parameters': [
        JWT_ACCESS_TOKEN,
        {
            'name': 'value',
            'description': '''
            잔류신청 상태
            1: 금요귀가
            2: 토요귀가
            3: 토요귀사
            4: 잔류
            ''',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '잔류신청 성공'
        },
        '204': {
            'description': '잔류신청 실패(신청 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
