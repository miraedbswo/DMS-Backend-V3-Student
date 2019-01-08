from app.doc import parameter, JWT_ACCESS_TOKEN

QNA_LIST_GET = {
    'tags': ['Notice'],
    'description': '자주 하는 질문 리스트 확인',
    'responses': {
        '200': {
            'description': '자주 하는 질문 리스트 조회 성공',
            'examples': {
                '': {
                    'qnaList': [
                        {
                            'title': '제목',
                            'postDate': '작성 일자',
                            'qnaId': '자주 하는 질문 아이디'
                        }
                    ]
                }
            }
        }
    }
}

QNA_GET = {
    'tags': ['Notice'],
    'description': '자주 하는 질문 확인',
    'parameters': [parameter('qnaId', '자주 하는 질문 아이디', 'url')],
    'responses': {
        '200': {
            'description': '자주 하는 질문 조회 성공',
            'examples': {
                '': {
                    'title': '제목',
                    'postDate': '작성 일자',
                    'content': '자주 하는 질문 내용'
                }
            }
        }
    }
}
