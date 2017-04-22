# -*- coding: UTF-8 -*-
from webapp import app


def log(msg):
    if not type(msg) == str:
        msg = str(msg)
    app.logger.info("[db Operations] " + msg)
