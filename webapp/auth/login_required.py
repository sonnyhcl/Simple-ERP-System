# -*- coding: UTF-8 -*-
from functools import wraps
from flask import request, redirect, url_for
from flask.globals import session

__author__ = 'sonnyhcl'


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function
