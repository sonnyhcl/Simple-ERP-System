# -*- coding: UTF-8 -*-
"""
社区页面的所有数据库操作
"""
import sqlite3
import traceback
from flask import session
from webapp.mylog import log

__author__ = 'sonnyhcl'


class Community(object):
    def add_community(self, c_name, u_id=0):
        """
        
        :param c_name: 
        :return: 'Success', '' or 'Fail', 'error_msg' 
        """
        log("%s: add community: %s %s" % (session['u_name'], c_name, u_id))
        conn = sqlite3.connect("demo.db")
        try:
            param = (c_name, u_id,)
            conn.execute('INSERT INTO community(c_name, u_id) VALUES (?, ?);',
                         param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def delete_community(self, c_id):
        """
        
        :param c_id: 
        :return: 'Success', '' or 'Fail', 'error_msg' 
        """
        log("%s: delete community: %s" % (session['u_name'], c_id))
        conn = sqlite3.connect("demo.db")
        # check if there is any users belonging to this community
        param = (c_id,)
        response = conn.execute('SELECT * FROM user WHERE c_id = ?;', param)
        response = response.fetchall()
        print response
        if not response == []:
            return "Fail", "There are still users belonging to community %s" \
                   % c_id
        try:
            param = (c_id,)
            conn.execute('DELETE FROM community WHERE c_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def update_community(self, c_id, new_c_name, u_id):
        """
        update_community
        :return: 'Success', '' or 'Fail', 'error_msg' 
        """
        log("%s: update community: %s %s %s"
            % (session['u_name'], c_id, new_c_name, u_id))
        conn = sqlite3.connect("demo.db")
        param = (new_c_name, u_id, c_id,)
        conn.execute('UPDATE community '
                     'SET c_name = ?, u_id = ? WHERE c_id = ?;',
                     param)
        conn.commit()
        conn.close()
        return "Success", ""

    def get_all_admin(self):
        """
        返回所有权限为admin & root的人的信息
        :return: 'Success', <response> or 'Fail', 'error_msg' 
        """
        conn = sqlite3.connect("demo.db")
        try:
            response = conn.execute('SELECT u_id, u_name FROM user '
                                    'WHERE u_role = ? OR u_role = ?;',
                                    ('root', 'admin'))
            response = response.fetchall()
        except Exception:
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", response

    def add_community_admin(self, c_id, u_id):
        """
        给当前未分配管理员的社区分配管理员，通常这一步伴随add community一起做
        :return: 'Success', '' or 'Fail', 'error_msg' 
        """
        log("%s: add_community_admin: %s %s" % (session['u_name'], c_id, u_id))
        conn = sqlite3.connect("demo.db")
        param = (u_id,)
        response = conn.execute('SELECT u_role FROM user WHERE user.u_id = ?',
                                param)
        response = response.fetchall()
        if (len(response) == 0) or response[0][0] != 'admin':
            conn.close()
            return "Fail", "%s is not root or admin" % u_id
        try:
            param = (u_id, c_id,)
            conn.execute('UPDATE community SET u_id = ? WHERE c_id = ?;', param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        conn.commit()
        conn.close()
        return "Success", ""

    def get_community_by_cid(self, c_id=0):
        """
        get_community_by_cid
        :return: 'Success', <response> or 'Fail', 'error_msg' 
        """
        conn = sqlite3.connect("demo.db")
        try:
            if c_id == 0:
                response = conn.execute(
                    'SELECT community.c_id, community.c_name, '
                    'user.u_name, user.u_phone, user.u_id '
                    'FROM community, user '
                    'WHERE user.u_id = community.u_id;')
            else:
                param = (c_id,)
                response = conn.execute(
                    'SELECT community.c_id, community.c_name, '
                    'user.u_name, user.u_phone, user.u_id '
                    'FROM community, user '
                    'WHERE community.c_id = ? AND user.u_id = community.u_id;',
                    param)
        except Exception:
            conn.close()
            return "Fail", traceback.print_exc()
        response = response.fetchall()
        conn.close()
        return "Success", response


community = Community()
