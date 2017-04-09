# coding: utf-8
import itchat
from flask import Flask, request
app = Flask(__name__)


@app.route('/webhooks', methods=['POST'])
def hello_world():
    event = request.get_json()
    commits = event.get('commits')
    groupid = u"sonnyhcl"
    if commits:
        msg = u'\ntimestamp: ' + commits[0].get('timestamp')
        author = commits[0].get('author')
        if author:
                msg += u'\npush_man: ' + author.get('username')
        else:
                msg += u'\npush_man: unknown'
        msg += u'\ncommits: ' + commits[0].get('message')
    else:
        msg = "this is not a commit message"
    print msg
    for i in itchat.get_chatrooms():
        for j in i['MemberList']:
            if j['NickName'] == u'leechen':
                groupid = i['UserName']
                break
    itchat.send(msg, groupid)
    return '0'

if __name__ == '__main__':
    itchat.auto_login(hotReload=True, enableCmdQR=1)
    app.run(host='0.0.0.0', debug=True)

# json.dumps(itchat.get_chatrooms(), indent=2)
