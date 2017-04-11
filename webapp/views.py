from webapp import app
from flask import render_template, request, session, flash, url_for, redirect
# from flask_login import login_required
from login_required import login_required
__author__ = 'sonnyhcl'


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/logout', methods=['POST'])
def logout():
    session['logged_in'] = False
    return "Bye"


def validate_user(uname, passwd):
    if not uname or not passwd:
        return False
    if not uname == 'hcl':
        return False
    if not passwd == 'hcl':
        return False
    return True


@app.route('/login', methods=['POST'])
def login():
    user_name = request.form.get('username', None)
    pass_word = request.form.get('password', None)
    next_url = request.form.get('next', url_for('index'))
    if validate_user(user_name, pass_word):
        session['logged_in'] = True
        return redirect(next_url)

    error_msg = "wrong username or password"
    return render_template('login_index.html', error=error_msg, next=next_url)


@app.route('/login_index', methods=['GET'])
def login_index():
    """
    http://localhost:5000/login_index?next=http%3A%2F%2Flocalhost%3A5000%2Ferror
    :return: templates
    """
    error_msg = None
    next_url = request.args.get('next', url_for('index'))
    print 'next: ' + next_url

    return render_template('login_index.html', error=error_msg, next=next_url)


@app.route('/error')
@login_required
def error():
    return render_template('error.html')


@app.route('/test')
def test():
    return redirect(url_for('static', filename='images/gold.png'))
