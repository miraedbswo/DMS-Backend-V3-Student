from test import TCBase


class TestExtensionInfo(TCBase):
    def __init__(self):
        super(TestExtensionInfo, self).__init__()

    def setUp(self):
        super(TestExtensionInfo, self).setUp()

    """
    default status 검증
    {
        'extension11': None
        'extension12': None,
        'goingOut': [None],
        'stay': 4
    }
    extension11, 12, goingOut, stay 설정 후 assertDictEqual
    """
