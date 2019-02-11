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

    SECRET_KEY = os.getenv('SECRET_KEY', 'Nerd-Bear')

    SWAGGER_TEMPLATE = {
        'schemes': [
            'https'
        ]
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@dms.istruly.sexy/dms-test'

    MAIL_SERVER = 'smtp.mailgun.org'
    MAIL_ID = 'dms@istruly.sexy'
    MAIL_PW = 'dmsM@ail2019'
    MAIL_PORT = 587


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)


class ProductionConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}
