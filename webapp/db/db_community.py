# -*- coding: UTF-8 -*-
"""
社区页面的所有数据库操作
"""

import sqlite3
from flask import session
from webapp.mylog import log
__author__ = 'sonnyhcl'


class Community(object):

    def add_community(self, c_name):
        """
        
        :param c_name: 
        :return: 'Success', '' or 'Fail', 'error_msg' 
        """
        # TODO: 社区名字判重
        # TODO 返回格式status, msg = ..... 以及异常处理
        log("%s: add community: %s" % (session['u_name'], c_name))
        conn = sqlite3.connect("test.db")
        param = (c_name, session['u_id'])
        conn.execute('INSERT INTO community(c_name, u_id) VALUES (?, ?);',
                     param)
        conn.commit()
        conn.close()
        return "Success"

    def delete_community(self, c_id):
        """
        
        :param c_id: 
        :return: 'Success', '' or 'Fail', 'error_msg' 
        """
        # TODO 返回格式status, msg = ..... 以及异常处理
        log("%s: delete community: %s" % (session['u_name'], c_id))
        conn = sqlite3.connect("test.db")
        param = (c_id,)
        conn.execute('DELETE FROM community WHERE c_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    def update_community(self, c_id, new_c_name, u_id):
        """
        
        :param c_id: 
        :param new_c_name: 
        :param u_id: 
        :return: 'Success', '' or 'Fail', 'error_msg' 
        """
        log("%s: update community: %s %s %s"
            % (session['u_name'], c_id, new_c_name ,u_id))
        conn = sqlite3.connect("test.db")
        param = (new_c_name, u_id, c_id)
        conn.execute('UPDATE community SET c_name = ?, u_id = ? WHERE c_id = ?;',
                     param)
        conn.commit()
        conn.close()
        return "Success"

    def get_all_admin(self):
        """
        返回所有权限为admin & root的人的信息
        :return: 'Success', <response> or 'Fail', 'error_msg' 
        """
        # TODO
        pass

    def add_community_admin(self, c_id, u_id):
        """
        给当前未分配管理员的社区分配管理员，通常这一步伴随add community一起做
        :param c_id: 
        :param u_id: 
        :return: 'Success', '' or 'Fail', 'error_msg' 
        """
        # TODO 返回格式status, msg = ..... 以及异常处理
        log("%s: add_community_admin: %s" % (session['u_name'], c_id, u_id))
        conn = sqlite3.connect("test.db")
        param = (u_id,)
        response = conn.execute('SELECT u_role FROM user WHERE user.u_id = ?',
                                param)
        response = response.fetchall()
        # TODO 这一步不应该出现错误,由community.get_all_admin()保证
        if (response is None) or response[0][0] != 'admin':
            conn.close()
            return "Fail"
        param = (u_id, c_id,)
        conn.execute('UPDATE community SET u_id = ? WHERE c_id = ?;', param)
        conn.commit()
        conn.close()
        return "Success"

    # def get_community(self, c_id):
    #     conn = sqlite3.connect("test.db")
    #     param = (c_id,)
    #     if c_id == 0:
    #         response = conn.execute('SELECT * FROM community;')
    #     else:
    #         response = conn.execute('SELECT * FROM community WHERE c_id = ?;',
    #                                 param)
    #     response = response.fetchall()
    #     conn.close()
    #     return "Success", response

    def get_community_by_cid(self, c_id):
        """
        
        :param c_id: 
        :return: 'Success', <response> or 'Fail', 'error_msg' 
        """
        # TODO 返回格式status, msg = ..... 以及异常处理
        conn = sqlite3.connect("test.db")
        if c_id == 0:
            response = conn.execute(
                'SELECT community.c_id, community.c_name, user.u_name, user.u_phone '
                'FROM community, user '
                'WHERE user.u_id = community.u_id;')
        else:
            param = (c_id,)
            response = conn.execute(
                'SELECT community.c_id, community.c_name, user.u_name, user.u_phone '
                'FROM community, user '
                'WHERE community.c_id = ? AND user.u_id = community.u_id;', param)
        response = response.fetchall()
        conn.close()
        return "Success", response

    # def get_all(self):
    #     conn = sqlite3.connect("test.db")
    #     response = conn.execute('SELECT * FROM community;')
    #     response = response.fetchall()
    #     conn.close()
    #     return "Success", response


community = Community()
