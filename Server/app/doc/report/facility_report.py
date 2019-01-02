from app.doc import SAMPLE_OBJECT_IDS, JWT_ACCESS_TOKEN, parameter

FACILITY_REPORT_POST = {
    'tags': ['Report'],
    'description': '시설고장신고',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('room', '호실 번호', type_='int'),
        parameter('content', '시설 고장 신고 내용')
    ],
    'responses': {
        '201': {
            'description': '시설고장 신고에 성공했으며, 업로드된 시설고장 신고의 ID를 응답합니다.',
            'examples': {
                '': {
                    'id': SAMPLE_OBJECT_IDS[0]
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
