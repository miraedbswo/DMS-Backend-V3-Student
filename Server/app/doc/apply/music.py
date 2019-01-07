from app.doc import JWT_ACCESS_TOKEN, parameter

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
                            'id': 1,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-07 11:27:25.689022'
                        },
                        {
                            'id': 10,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-02-07 11:27:25.689022'
                        }
                    ],
                    'tue': [
                        {
                            'id': 2,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-03-07 11:27:25.689022'
                        },
                        {
                            'id': 3,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-04-07 11:27:25.689022'
                        }
                    ],
                    'wed': [
                        {
                            'id': 4,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-03 11:27:25.689022'
                        },
                        {
                            'id': 5,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-08 11:27:25.689022'
                        }
                    ],
                    'thu': [
                        {
                            'id': 6,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-17 11:27:25.689022'
                        },
                        {
                            'id': 7,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-27 11:27:25.689022'
                        }
                    ],
                    'fri': [
                        {
                            'id': 8,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-12 11:27:25.689022'
                        },
                        {
                            'id': 9,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-23 11:27:25.689022'
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
        parameter('singer', '가수 이름'),
        parameter('musicName', '노래 이름')
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

