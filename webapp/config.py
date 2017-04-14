# -*- coding: UTF-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'
    LOG_FILE_NAME = 'error.log'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'root'
    MYSQL_DATABASE_DB = 'web'
    CONFIG_PATH = os.path.abspath(os.path.dirname(__file__))
    PROJ_PATH = os.path.split(CONFIG_PATH)[0]

    def __init__(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0p s3cr3t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    MAIL_FLUSH_INTERVAL = 60  # one minute


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': Config
}
