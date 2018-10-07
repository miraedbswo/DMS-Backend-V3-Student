SIGNUP_POST = {
    'tags': ['Account'],
    'description': '회원가입',
    'parameters': [
        {
            'name': 'uuid',
            'description': 'UUID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '사용자 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'password',
            'description': '사용자 PW',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '가입 완료'
        },
        '204': {
            'description': '가입 불가능(유효하지 않은 UUID)'
        },
        '409': {
            'description': '가입 불가능(중복된 ID)'
        }
    }
}
