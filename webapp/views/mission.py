# -*- coding: UTF-8 -*-
import json
from flask import render_template, session, request
from webapp import app
from db.db_community import *

__author__ = 'sonnyhcl'

@app.route('/mission', methods=['GET'])
def mission_index():
    return render_template('mission.html')
