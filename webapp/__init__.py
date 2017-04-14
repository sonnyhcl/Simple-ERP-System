# -*- coding: UTF-8 -*-
import os
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask
app = Flask(__name__)

from webapp import views
from config import config
from db import *
from models import *

__author__ = 'sonnyhcl'

db = MySQL()
bootstrap = Bootstrap()
moment = Moment()

db.init_app(app)
bootstrap.init_app(app)
moment.init_app(app)

app.config.from_object(config[os.getenv('FLASK_CONFIG') or 'default'])
if app.config['DEBUG']:
    import logging
    log_path = os.path.join(app.config['PROJ_PATH'], 'logs')
    log_file = os.path.join(log_path, 'webapp.log')
    # print log_path, log_file
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] %(filename)s:%(lineno)d\t' +
                               '%(levelname)s\t %(message)s',
                        datefmt='%Y.%m.%d %H:%M:%S',
                        filename=log_file,
                        filemode='a')
    from logging.handlers import SysLogHandler
    syslog_handler = SysLogHandler()
    syslog_handler.setLevel(logging.WARNING)
    app.logger.addHandler(syslog_handler)


def log_out(msg):
    if app.config['DEBUG']:
        app.logger.debug(msg)
