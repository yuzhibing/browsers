from flask import Flask
from create_db import *

def ut_price(period):
    row_list = []
    try:
        ud_price_query = ''
        if period == 'day':
            ud_price_query = " select UNIX_TIMESTAMP(create_time)*1000,sum(price)/count(*),DATE_FORMAT(create_time,'%Y-%m-%d %h:00:00') from ud_price where create_time>DATE_ADD(NOW(),INTERVAL -1 DAY) group by DATE_FORMAT(create_time,'%Y-%m-%d %h') order by create_time asc"
        elif period == 'week':
            ud_price_query = " select UNIX_TIMESTAMP(create_time)*1000,sum(price)/count(*),DATE_FORMAT(create_time,'%Y-%m-%d %h:00:00') from ud_price where create_time>DATE_ADD(NOW(),INTERVAL -7 DAY) group by DATE_FORMAT(create_time,'%Y-%m-%d %h') order by create_time asc"
        elif period == 'month':
            ud_price_query = " select UNIX_TIMESTAMP(create_time)*1000,sum(price)/count(*),DATE_FORMAT(create_time,'%Y-%m-%d 00:00:00') from ud_price where create_time>DATE_ADD(NOW(),INTERVAL -30 DAY) group by DATE_FORMAT(create_time,'%Y-%m-%d') order by create_time asc"

        res = db.session.execute(ud_price_query)
        row_list = res.fetchall()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print e

    price_list = []
    if row_list != None:

        for index in range(len(row_list)):
            list = []
            list.append(row_list[index][0])
            list.append(row_list[index][1])
            price_list.append(list)


    return price_list