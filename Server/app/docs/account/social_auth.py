from app.docs.account import SAMPLE_ACCESS_TOKEN, SAMPLE_REFRESH_TOKEN
from app.docs import JWT_ACCESS_TOKEN

ADD_SOCIAL_ACCOUNT_POST = {
    'tags': ['Account'],
    'description': '소셜 계정 연동 (아직 어떻게 될 지 모름)',
    'parameters': [
        JWT_ACCESS_TOKEN,
        {
            'name': 'socialPlatform',
            'description': '소셜 계정 플랫폼',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'uuid',
            'description': '소셜 계정 구분자',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '소셜 계정 연동 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

SOCIAL_AUTH_POST = {
    'tags': ['Account'],
    'description': '소셜 계정 로그인 (아직 어떻게 될 지 모름)',
    'parameters': [
        {
            'name': 'uuid',
            'description': '소셜 계정 구분자',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '소셜 로그인 성공',
            'examples': {
                '': {
                    'accessToken': SAMPLE_ACCESS_TOKEN,
                    'refreshToken': SAMPLE_REFRESH_TOKEN
                }
            }
        },
        '401': {
            'description': '소셜 로그인 실패'
        }
    }
}
