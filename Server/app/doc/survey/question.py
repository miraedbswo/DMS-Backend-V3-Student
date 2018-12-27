from app.doc import JWT_ACCESS_TOKEN, SAMPLE_OBJECT_IDS

QUESTION_GET = {
    'tags': ['Survey'],
    'description': '설문지 질문 리스트를 불러옵니다.',
    'parameters': [
        JWT_ACCESS_TOKEN,
        {
            'name': 'surveyId',
            'description': '설문지 ID',
            'in': 'url',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '질문 리스트 불러오기 성공. 답변했다면 답변도 함께 반환됩니다.',
            'examples': {
                '': [
                    {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'title': '저녁에 치킨을 먹고 싶습니까?',
                        'isObjective': True,
                        'choicePaper': ['예', '아니오'],
                        'answer': '예'
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'title': '어디 치킨이 좋습니까?',
                        'isObjective': False,
                        'answer': None
                    }
                ]
            }
        },
        '204': {
            'description': '존재하지 않는 설문지 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

QUESTION_POST = {
    'tags': ['Survey'],
    'description': '질문에 답변을 남깁니다. 이미 답변을 남겼을 경우, 덮어씌웁니다.',
    'parameters': [
        JWT_ACCESS_TOKEN,
        {
            'name': 'questionId',
            'description': '질문 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'answerContent',
            'description': '답변',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '답변 남기기 성공'
        },
        '204': {
            'description': '존재하지 않는 질문 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
