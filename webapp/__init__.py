# -*- coding: UTF-8 -*-
import os
from flask import Flask
from config import config
app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_CONFIG') or 'default'])
__author__ = 'sonnyhcl'

import logging
log_path = os.path.join(app.config['PROJECT_PATH'], 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_file = os.path.join(log_path, 'webapp.log')
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    filename=log_file,
                    filemode='a')
from logging.handlers import SysLogHandler
syslog_handler = SysLogHandler()
syslog_handler.setLevel(logging.DEBUG)
app.logger.addHandler(syslog_handler)

from mylog import log
from webapp import views
from webapp import auth
from webapp import db