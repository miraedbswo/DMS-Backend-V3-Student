from app.doc import parameter
from app.doc.account import SAMPLE_ACCESS_TOKEN, SAMPLE_REFRESH_TOKEN

AUTH_POST = {
    'tags': ['Account'],
    'description': '로그인',
    'parameters': [
        parameter('id', '아이디'),
        parameter('password', '비밀번호')
    ],
    'responses': {
        '200': {
            'description': '로그인 성공',
            'examples': {
                '': {
                    'accessToken': SAMPLE_ACCESS_TOKEN,
                    'refreshToken': SAMPLE_REFRESH_TOKEN
                }
            }
        },
        '401': {
            'description': '로그인 실패'
        }
    }
}
