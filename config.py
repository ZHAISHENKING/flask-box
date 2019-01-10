import os
import datetime
from production import *
try:
    from local_settings import *
except Exception:
    pass


class Config(object):
    DEBUG = False
    TESTING = False

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SECRET_KEY = 'FDANFSDAOssdadE1-013UR12y4ibksd13B2KJ;SC0231'
    REMEMBER_COOKIE_DURATION = datetime.timedelta(hours=3)
    BABEL_DEFAULT_LOCALE = 'zh_CN'

    RESTFUL_JSON = dict(ensure_ascii=False)

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'demo',
        'host': 'localhost'
    }


class PrdConfig(Config):
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'demo',
        'host': 'localhost',
        'port': PORT,
        "username": NAME,
        "password": PWD
    }


class TestingConfig(Config):
    TESTING = True
    DEBUG = True

    WTF_CSRF_ENABLED = False
    MONGODB_SETTINGS = {
        'db': 'Courses_test',
        'is_mock': True
    }


config = {
    'dev': DevConfig,
    'prd': PrdConfig,
    'testing': TestingConfig,
    'default': DevConfig,
}


