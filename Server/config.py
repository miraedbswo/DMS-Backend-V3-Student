import os
from datetime import timedelta


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

    SECRET_KEY = os.getenv('SECRET_KEY')

    JSON_AS_ASCII = False

    SWAGGER_TEMPLATE = {
        'schemes': [
            'https'
        ]
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

    MAIL_SERVER = 'smtp.mailgun.org'
    MAIL_ID = 'dms@istruly.sexy'
    MAIL_PW = 'dmsM@ail2019'
    MAIL_PORT = 587

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(weeks=2)
    PROPAGATE_EXCEPTIONS = True


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=100)


class ProductionConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}
