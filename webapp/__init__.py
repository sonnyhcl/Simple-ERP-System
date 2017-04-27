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
web_log_file = os.path.join(log_path, app.config['LOG_FILE_NAME'])
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    filename=web_log_file,
                    filemode='a')
from logging.handlers import SysLogHandler
syslog_handler = SysLogHandler()
syslog_handler.setLevel(logging.DEBUG)
app.logger.addHandler(syslog_handler)

db_log_file = os.path.join(log_path, 'db_operator.log')
handler = logging.FileHandler(db_log_file)
app.logger.addHandler(handler)

from mylog import log
from webapp import views
# from webapp import auth
# from webapp import db
