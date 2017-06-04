# -*- coding:utf-8 -*-
__author__ = 'Jevade'
__data__ = '2017/5/29 11:12'

from logging import log
from flask import  Flask
from flask import  request

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"

@app.route('/wx')
def wx():
    echostr = request.args.get('echostr')
    
    return echostr


if "__name__" == "__main__":
    app.run(host='0.0.0.0',debug=True)