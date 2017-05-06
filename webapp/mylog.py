# -*- coding: UTF-8 -*-
from time import asctime
from flask import session
from webapp import app

__author__ = 'sonnyhcl'


def log(msg):
    if type(msg) == str or type(msg) == unicode:
        app.logger.info("[%s]%s: %s" %
                        (asctime(), session.get('u_name'), msg))
