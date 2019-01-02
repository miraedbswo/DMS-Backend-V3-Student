from app.doc import JWT_ACCESS_TOKEN, parameter


QUESTION_POST = {
    'tags': ['Survey'],
    'description': '질문에 답변을 남깁니다. 이미 답변을 남겼을 경우, 덮어씌웁니다.',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('questionId', '질문 아이디'),
        parameter('answerContent', '답변')
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
