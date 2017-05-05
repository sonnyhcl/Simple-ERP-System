# -*- coding: UTF-8 -*-
from functools import wraps
from flask import session, abort
__author__ = 'sonnyhcl'

level = {'guest': 0, 'user': 1, 'admin': 2, 'root': 3}


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            role = session.get('u_role', 'guest')
            if level[role] < level[permission]:
                abort(404)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
