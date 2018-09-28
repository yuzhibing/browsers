#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask,jsonify,request
from api.order import *
from api.address import *
from api.ut_price import *
from api.transaction import *


app = Flask(__name__)


###大单监控
@app.route("/api/v1/monitor/order")
def order():

    order_list = query_big_order()
    return jsonify(order_list)

####地址监控
@app.route("/api/v1/monitor/address")
def address():
    address_list = query_address()
    return jsonify(address_list)

###ut价格
@app.route("/api/v1/monitor/price")
def price():
    period = request.values.get('period')
    price = ut_price(period)
    return jsonify(price)

###交易数度
@app.route("/api/v1/monitor/transaction")
def transaction():
    f = request.values.get('f')
    speed = trans_speed(f)
    return jsonify(speed)

def start():

    print("start web server at 5000")
    app.run(host='0.0.0.0', port=5000)



if __name__ == '__main__':
    start()
