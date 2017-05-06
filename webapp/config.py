# -*- coding: UTF-8 -*-
import os

__author__ = 'sonnyhcl'
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    SECRET_KEY = 'hard to guess'
    LOG_FILE_NAME = 'webapp.log'
    CONFIG_PATH = os.path.abspath(os.path.dirname(__file__))
    PROJECT_PATH = os.path.split(CONFIG_PATH)[0]

    def __init__(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0p s3cr3t'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'secret'


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'show me your code'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
