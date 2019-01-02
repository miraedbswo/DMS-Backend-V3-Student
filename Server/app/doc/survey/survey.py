from app.doc import SAMPLE_OBJECT_IDS, JWT_ACCESS_TOKEN, parameter

SURVEY_LIST_GET = {
    'tags': ['Survey'],
    'description': '''설문지 리스트를 불러옵니다.
    아래의 조건 중 하나 이상에 맞는 설문조사는 response되지 않습니다.
    
    1. 대상이 해당 학년이 아닌 설문조사
    2. 설문 기간이 지난 설문조사
    3. 질문이 없는 설문조사
    ''',
    'parameters': [JWT_ACCESS_TOKEN],
    'responses': {
        '200': {
            'description': '설문지 리스트 불러오기 성공',
            'examples': {
                '': [
                    {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'title': '인상민 생일 선물 뭐 줄까?',
                        'startDate': '2018-04-15',
                        'endDate': '2018-04-20',
                        'answered': True
                    },
                    {
                        'id': SAMPLE_OBJECT_IDS[1],
                        'title': '아침운동 시행 찬반 설문조사',
                        'startDate': '2018-03-02',
                        'endDate': '2018-12-31',
                        'answered': False
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}


SURVEY_GET = {
    'tags': ['Survey'],
    'description': '''설문지를 불러옵니다.
    아래의 조건 중 하나 이상에 맞는 설문조사는 response되지 않습니다.

    1. 대상이 해당 학년이 아닌 설문조사
    2. 설문 기간이 지난 설문조사
    3. 질문이 없는 설문조사
    ''',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('survey_id', '설문지 id', 'url', 'int')
    ],
    'responses': {
        '200': {
            'description': '설문지 불러오기 성공',
            'examples': {
                '': {
                        'id': SAMPLE_OBJECT_IDS[0],
                        'title': '인상민 생일 선물 뭐 줄까?',
                        'description': '4월 20일은 인상민 생일인데 인상민한테 생일 선물 뭐 줄거예요?',
                        'startDate': '2018-04-15',
                        'endDate': '2018-04-20',
                        'answered': True,
                        'questions': [
                            {
                                'id': '질문 아이디1',
                                'title': '저녁에 치킨을 먹고 싶습니까?',
                                'isObjective': True,
                                'choicePaper': ['예', '아니오'],
                                'answer': '예'
                            },
                            {
                                'id': '질문 아이디 2',
                                'title': '어디 치킨이 좋습니까?',
                                'isObjective': False,
                                'answer': None
                            }
                        ]
                    }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}