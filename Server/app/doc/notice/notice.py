from app.doc import parameter, JWT_ACCESS_TOKEN

NOTICE_LIST_GET = {
    'tags': ['Notice'],
    'description': '공지사항 리스트 확인',
    'parameters': [JWT_ACCESS_TOKEN],
    'responses': {
        '200': {
            'description': '공지사항 리스트 조회 성공',
            'examples': {
                '': {
                    'noticeList': [
                        {
                            'title': '제목',
                            'postDate': '작성 일자',
                            'noticeId': '공지사항 아이디'
                        }
                    ]
                }
            }
        }
    }
}

NOTICE_GET = {
    'tags': ['Notice'],
    'description': '공지사항 확인',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('noticeId', '공지사항 아이디', 'url')
    ],
    'responses': {
        '200': {
            'description': '공지사항 조회 성공',
            'examples': {
                '': {
                    'title': '제목',
                    'postDate': '작성 일자',
                    'content': '공지사항 내용'
                }
            }
        }
    }
}
