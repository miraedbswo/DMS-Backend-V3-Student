from app.docs import JWT_ACCESS_TOKEN


CHANGE_PW_PATCH = {
    'tags': ['Account'],
    'description': '비밀번호 변경',
    'parameters': [
        JWT_ACCESS_TOKEN,
        {
            'name': 'currentPassword',
            'description': '현재 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'newPassword',
            'description': '바꿀 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '비밀번호 변경 성공'
        },
        '205': {
            'description': '현재 비밀번호와 새 비밀번호가 동일함'
        },
        '403': {
            'description': '비밀번호 변경 실패(틀린 비밀번호), 또는 권한 없음'
        }
    }
}

