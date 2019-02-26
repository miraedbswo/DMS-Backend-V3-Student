from app.doc import parameter

RULE_LIST_GET = {
    'tags': ['Notice'],
    'description': '기숙사 규정 리스트 확인',
    'responses': {
        '200': {
            'description': '기숙사 규정 리스트 조회 성공',
            'examples': {
                '': {
                    'ruleList': [
                        {
                            'title': '제목',
                            'postDate': '작성 일자',
                            'ruleId': '기숙사 규정 아이디'
                        }
                    ]
                }
            }
        }
    }
}

RULE_GET = {
    'tags': ['Notice'],
    'description': '기숙사 규정 확인',
    'parameters': [parameter('ruleId', '기숙사 규정 아이디', 'url')],
    'responses': {
        '200': {
            'description': '기숙사 규정 조회 성공',
            'examples': {
                '': {
                    'title': '제목',
                    'postDate': '작성 일자',
                    'content': '기숙사 규정 내용'
                }
            }
        }
    }
}
