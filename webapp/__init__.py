# -*- coding: UTF-8 -*-
import os
from flask import Flask
import logging
from logging.handlers import SysLogHandler
app = Flask(__name__)

from webapp import views
from webapp import auth
from webapp import db
from config import config

__author__ = 'sonnyhcl'

database = db.MySQL()
database.init_app(app)

app.config.from_object(config[os.getenv('FLASK_CONFIG') or 'default'])
log_path = os.path.join(app.config['PROJ_PATH'], 'logs')
log_file = os.path.join(log_path, 'webapp.log')
if not os.path.exists(log_path):
    os.mkdir(log_path)
logging.basicConfig(level=logging.WARNING,
                    format='[%(asctime)s]\t' +
                           '%(levelname)s\t %(message)s',
                    datefmt='%Y.%m.%d %H:%M:%S',
                    filename=log_file,
                    filemode='a')
syslog_handler = SysLogHandler()
syslog_handler.setLevel(logging.WARNING)
app.logger.addHandler(syslog_handler)


def log_msg(msg):
    if app.config['DEBUG']:
        app.logger.warning(msg)
