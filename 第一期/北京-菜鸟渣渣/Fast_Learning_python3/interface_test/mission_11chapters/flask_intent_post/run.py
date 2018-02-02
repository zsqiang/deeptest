#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

from flask import Flask
from flask import render_template, redirect,url_for
from flask import request

app = Flask(__name__)
print(app)
@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']=='Young':
            return redirect(url_for('home',username=request.form['username']))
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html', username=request.args.get('username'))

if __name__ != '__main__':
    app.debug = True
    app.run()