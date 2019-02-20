from app.doc import JWT_ACCESS_TOKEN, parameter

EXTENSION_GET = {
    'tags': ['Apply'],
    'description': '학생 자신의 연장신청 정보를 조회합니다.',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('time', '11시, 12시 연장 구분 (11, 12)', 'url', 'int')
    ],
    'responses': {
        '200': {
            'description': '연장신청 정보 조회 성공',
            'examples': {
                '': {
                    'classNum': 1,
                    'seatNum': 16
                }
            }
        },
        '204': {
            'description': '연장신청 정보 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

EXTENSION_POST = {
    'tags': ['Apply'],
    'description': '''연장신청
    11시 연장 신청 가능 시간: 17:30 - 20:30
    12시 연장 신청 가능 시간: 17:30 - 22:00
    ''',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('time', '11시, 12시 연장 구분 (11, 12)', 'url', 'int'),
        {
            'name': 'classNum',
            'description': '''
            연장 학습실 번호
            1: 가온실
            2: 나온실
            3: 다온실
            4: 라온실
            5: 3층 독서실
            6: 4층 독서실
            7: 5층 열린교실
            ''',
            'in': 'json',
            'type': 'int',
            'required': True
        },
        parameter('seatNum', '연장학습 자리 번호', type_='int')
    ],
    'responses': {
        '201': {
            'description': '연장신청 성공'
        },
        '205': {
            'description': '이미 신청된 자리거나, 신청할 수 없는 곳(범위를 넘어섬)'
        },
        '409': {
            'description': '연장신청 실패(신청 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

EXTENSION_DELETE = {
    'tags': ['Apply'],
    'description': '''연장 신청을 취소합니다.
    
    11시 연장 신청 취소 가능 시간: 17:30 - 20:30
    12시 연장 신청 취소 가능 시간: 17:30 - 22:00
    ''',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('time', '11시, 12시 연장 구분 (11, 12)', 'url', 'int')
    ],
    'responses': {
        '200': {
            'description': '연장신청 취소 성공'
        },
        '403': {
            'description': '권한 없음'
        },
        '409': {
            'description': '연장신청 취소 실패(취소 가능 시간 아님)'
        }
    }
}

EXTENSION_MAP_GET = {
    'tags': ['Apply'],
    'description': '연장신청 지도를 조회합니다. 해당 class에 대한 신청 여부, 신청되어 있다면 자리까지 response합니다. 신청되어 있지 않으면 자리는 0입니다.',
    'parameters': [
        parameter('time', '11시, 12시 연장 구분 (11, 12)', 'url', 'int'),
        parameter('classNum', '조회할 학습실 번호', 'url', 'int')
    ],
    'responses': {
        '200': {
            'description': '지도 조회 성공',
            'examples': {
                '': {
                    'map': [
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0],
                        ['김윤재', 0, 1, 0, 0]
                    ]
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
