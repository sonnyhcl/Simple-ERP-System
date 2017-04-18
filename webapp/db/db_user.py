# -*- coding: UTF-8 -*-


def validate_user(uname, passwd):
    if not uname or not passwd:
        return False
    if not uname == 'hcl':
        return False
    if not passwd == 'hcl':
        return False
    return True
