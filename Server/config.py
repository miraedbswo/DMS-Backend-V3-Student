from os import getenv


class Config:
    SERVICE_NAME = 'DMS-V3'
    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'https'
        ]
    }


class TestConfig(Config):
    pass
