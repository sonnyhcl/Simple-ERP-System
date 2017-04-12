#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from flask_bootstrap import Bootstrap
# from flaskext.mysql import MySQL
from flask_moment import Moment
from flask import Flask
app = Flask(__name__)

from webapp import views
from config import config
from db import *
from models import *

__author__ = 'sonnyhcl'

bootstrap = Bootstrap()
db = MySQL()
moment = Moment()

db.init_app(app)
bootstrap.init_app(app)
moment.init_app(app)

app.config.from_object(config[os.getenv('FLASK_CONFIG') or 'default'])
if app.config['DEBUG']:
    import logging
    log_path = app.config['PROJ_PATH'] + '\logs'
    log_file = log_path + '\webapp.log'
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] ' +
                               '%(levelname)s\t %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=log_file,
                        filemode='a')
    from logging.handlers import SysLogHandler
    syslog_handler = SysLogHandler()
    syslog_handler.setLevel(logging.WARNING)
    app.logger.addHandler(syslog_handler)


def log_out(msg):
    if app.config['DEBUG']:
        app.logger.debug(msg)
