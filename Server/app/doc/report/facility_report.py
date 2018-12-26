from app.doc import SAMPLE_OBJECT_IDS, JWT_ACCESS_TOKEN

FACILITY_REPORT_POST = {
    'tags': ['Report'],
    'description': '시설고장신고',
    'parameters': [
        JWT_ACCESS_TOKEN,
        {
            'name': 'content',
            'description': '시설고장신고 내용',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'room',
            'description': '호실 번호',
            'in': 'json',
            'type': 'int',
            'required': True
        }
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
