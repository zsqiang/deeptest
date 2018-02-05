# coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

# 构建的mock server进行API实例演示。

'''
选型

为了让大家了解python的强大，我们flask来做一个简单的server

如果你需要更多的了解flask请参见官方中文文档:

http://docs.jinkan.org/docs/flask
'''

'''
安装flaask

pip install flask
支持

支持GET, POST, PUT, PATCH, DELETE 等http方法
'''
'''
from flask.app import  Flask

print(__name__)
app=Flask(__name__)

@app.route('/index')
def index():
    return  'hello World'

if __name__ != '__main__':
    app.run()


'''

from  flask import Flask
from  flask import jsonify
from flask import request, Response
import random, time

app = Flask(__name__)
"""
    这里所有的接口我们才去返回json串
    所有的json传对应的value值都为随机的
"""


# generate random-str


def random_str():
    data = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    # 用时间来做随机播种
    random.seed(time.time())

    sa = []

    for i in range(8):
        sa.append(random.choice(data))
    salt = "".join(sa)

    return (salt)


# 构建response
def make_response():
    content = '{"result": "%s", "data": "%s"}' % (random_str(), random_str())
    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'
    print(resp)

    return resp


# http GET
@app.route("/query", methods=["GET"])
def query():
    return jsonify(username=random_str(), password=random_str())


# http POST

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    if request.method == "POST":
        return "ok"
        # return make_response()


@app.route("/delete", methods=['DELETE'])
def delete():
    return make_response()


# HTTP HEAD

@app.route("/head", methods=['HEAD'])
def head():
    return make_response()


'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below this is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
'''

from flask import Flask
from flask import jsonify
from flask import request, Response
import random

time

app = Flask(__name__)

"""
    这里所有的接口我们才去返回json串
    所有的json传对应的value值都为随机的
"""


# 生成随机字符串
def random_str():
    # 待选随机数据
    data = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"

    # 用时间来做随机播种
    random.seed(time.time())

    # 随机选取数据
    sa = []
    for i in range(8):
        sa.append(random.choice(data))
    salt = ''.join(sa)

    return salt


# 构建response
def make_response():
    content = '{"result": "%s", "data": "%s"}' % (random_str(), random_str())

    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'

    return resp


# http GET
@app.route("/query", methods=["GET"])
def query():
    return jsonify(
        username=random_str(),
        password=random_str()
    )


# http POST
@app.route("/update", methods=["POST"])
def update():
    return make_response()


# http delete
@app.route("/delete", methods=["DELETE"])
def delete():
    return make_response()


# http head
@app.route("/head", methods=["HEAD"])
def head():
    return make_response()


if __name__ == "__main__":
    app.run(debug=True)

    '''
    注意POST\HEAD\DELETE方法，响应头均被加入了Access-Control-Origin属性，其值为：*

注意即便给HEAD方法添加了响应内容，但你在实际接收到的内容是木有响应内容的，请思考为什么

上述仅用于简单的测试，不讨论其优雅、靠谱、高大上等等可能性
'''
