# -*- coding: UTF-8 -*-
from webapp import app


def log(msg):
    if type(msg) == str or type(msg) == unicode:
        app.logger.info("[db Operations] " + msg)
