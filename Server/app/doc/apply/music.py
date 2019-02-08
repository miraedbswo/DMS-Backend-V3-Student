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
                            'applyDate': '2019-01-07 11:27:25.689022',
                            'studentId': 'asdf222'
                        },
                        {
                            'id': 10,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-02-07 11:27:25.689022',
                            'studentId': 'asdf111'
                        }
                    ],
                    'tue': [
                        {
                            'id': 2,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-03-07 11:27:25.689022',
                            'studentId': 'asdf444'
                        },
                        {
                            'id': 3,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-04-07 11:27:25.689022',
                            'studentId': 'asdf12'
                        }
                    ],
                    'wed': [
                        {
                            'id': 4,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-03 11:27:25.689022',
                            'studentId': 'asd63f'
                        },
                        {
                            'id': 5,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-08 11:27:25.689022',
                            'studentId': 'as321df'
                        }
                    ],
                    'thu': [
                        {
                            'id': 6,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-17 11:27:25.689022',
                            'studentId': 'asd123f'
                        },
                        {
                            'id': 7,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-27 11:27:25.689022',
                            'studentId': 'asredf'
                        }
                    ],
                    'fri': [
                        {
                            'id': 8,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-12 11:27:25.689022',
                            'studentId': 'asedf'
                        },
                        {
                            'id': 9,
                            'studentName': '누구누구',
                            'singer': 'aaa',
                            'musicName': 'aaa',
                            'applyDate': '2019-01-23 11:27:25.689022',
                            'studentId': 'asdfd'
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
    초기화 시간: 금요일 12:00
    ''',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('day', '요일', type_='int'),
        parameter('singer', '가수 이름'),
        parameter('musicName', '노래 이름')
    ],
    'responses': {
        '201': {
            'description': '기상음악 신청 성공'
        },
        '205': {
            'description': '기상음악 신청이 모두 완료되어 신청할 수 없음'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

MUSIC_DELETE = {
    'tags': ['Apply'],
    'description': '기상음악 신청 취소',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('applyId', '신청 아이디', type_='int')
    ],
    'responses': {
        '200': {
            'description': '기상음악 신청 성'
        },
        '204': {
            'description': '없는 apply id'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
