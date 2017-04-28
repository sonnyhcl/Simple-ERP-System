# -*- coding: UTF-8 -*-
from time import asctime
from flask import session
from webapp import app


def log(msg):
    if type(msg) == str or type(msg) == unicode:
        app.logger.info("[%s]%s: %s" %
                        (asctime(), session['u_name'], msg))
