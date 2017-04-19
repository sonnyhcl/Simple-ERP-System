# -*- coding: UTF-8 -*-
from webapp import app


def log(msg):
    if not type(msg) == str:
        return
    app.logger.info("[User Operations] " + msg)
