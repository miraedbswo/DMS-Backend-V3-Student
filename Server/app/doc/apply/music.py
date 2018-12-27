from app.doc import JWT_ACCESS_TOKEN

MUSIC_GET = {
    'tags': ['Apply'],
    'description': '현재 신청된 기상음악 신청 정보를 조회합니다.',
    'responses': {
        '200': {
            'description': '기상음악 신청 정보 조회 성공',
            'examples': {
                '': {
                    'mon': [
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        },
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        }
                    ],
                    'tue': [
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        },
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        }
                    ],
                    'wed': [
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        },
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        }
                    ],
                    'thu': [
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        },
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        }
                    ],
                    'fri': [
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        },
                        {
                            'student_name': '누구누구',
                            'singer': 'aaa',
                            'music_name': 'aaa'
                        }
                    ]
                }
            }
        },
        '204': {
            'description': '기상음악 신청 정보 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

MUSIC_POST = {
    'tags': ['Apply'],
    'description': '''기상음악 신청
    
    신청 시간: 일요일 20:30 - 금요일 12:00
    초기화 시간: 금요일 12:00
    ''',
    'parameters': [
        JWT_ACCESS_TOKEN,
        {
            'name': 'singer',
            'description': '가수 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'music_name',
            'description': '노래 이름',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '기상음악 신청 성공'
        },
        '204': {
            'description': '기상 음악 신청 실패(신청 가능 시간 아님)'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

