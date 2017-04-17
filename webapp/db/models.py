# -*- coding: UTF-8 -*-


def validate_user(uname, passwd):
    if not uname or not passwd:
        return False
    if not uname == 'hcl':
        return False
    if not passwd == 'hcl':
        return False
    return True


class User(object):
    """
    用户信息表
    """
    def add_user(self):
        pass

    def delete_user(self):
        pass

    def update_user(self):
        pass

    def get_user(self):
        pass

    def get_all(self):
        pass


class Community(object):
    """
    社区信息表
    """
    def add_community(self):
        pass

    def delete_community(self):
        pass

    def update_community(self):
        pass

    def get_community(self):
        pass

    def get_all(self):
        pass


class Item(object):
    """
    工艺信息表
    """
    def add_item(self):
        pass

    def delete_item(self):
        pass

    def update_item(self):
        pass

    def get_item(self):
        pass

    def get_all(self):
        pass


class Transaction(object):
    """
    流水信息表
    """
    def add_transaction(self):
        pass

    def delete_transaction(self):
        pass

    def update_transaction(self):
        pass

    def get_transaction(self):
        pass

    def get_all(self):
        pass


class Production(object):
    """
    产品信息表
    """
    def add_production(self):
        pass

    def delete_production(self):
        pass

    def update_production(self):
        pass

    def get_production(self):
        pass

    def get_all(self):
        pass
