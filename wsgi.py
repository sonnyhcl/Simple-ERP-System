# -*- coding: UTF-8 -*-
from flask import Flask
from werkzeug.serving import run_simple
__author__ = 'sonnyhcl'

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    run_simple('localhost', 5555, app,
               use_reloader=True, use_debugger=True, use_evalex=True)
