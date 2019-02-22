from app.doc import parameter

SIGNUP_POST = {
    'tags': ['Account'],
    'description': '회원가입',
    'parameters': [
        parameter('uuid', 'UUID'),
        parameter('id', '사용자 아이디'),
        parameter('password', '사용자 비밀번호')
    ],
    'responses': {
        '201': {
            'description': '가입 완료'
        },
        '204': {
            'description': '가입 불가능(유효하지 않은 UUID)'
        },
        '205': {
            'description': '가입 불가능(중복된 ID)'
        }
    }
}
