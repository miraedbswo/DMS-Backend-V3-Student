import os


class Config:
    SERVICE_NAME = 'DMS-V3'
    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
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


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///:memory:'


class ProductionConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}
