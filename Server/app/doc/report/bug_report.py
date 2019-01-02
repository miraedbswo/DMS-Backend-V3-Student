from app.doc import JWT_ACCESS_TOKEN, parameter

BUG_REPORT_POST = {
    'tags': ['Report'],
    'description': '버그를 신고하며, Slackbot이 Slack의 #bug-report 채널로 메시지를 전송합니다.',
    'parameters': [
        JWT_ACCESS_TOKEN,
        parameter('platform', '버그 신고를 한 플랫폼 타입(1: Web, 2: Android, 3: iOS)', 'url', 'int'),
        parameter('content', '버그 신고 내용')
    ],
    'responses': {
        '201': {
            'description': '버그 신고 성공'
        },
        '400': {
            'description': 'platform 타입이 1, 2, 3 중 하나가 아님'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
