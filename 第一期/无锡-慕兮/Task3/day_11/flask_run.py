# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

from flask import Flask

app = Flask(__name__)

@app.route('/api')
def index():
    return "hello world!"

if __name__ == '__main__':
    app.run()