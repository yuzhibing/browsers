from flask import Flask
from create_db import *

def query_big_order():
    row_list = []
    try :
       # big_order_query = " select address,value,DATE_FORMAT(mined_time,   '%Y-%m-%d %H:%i:%S'),has_vin,UNIX_TIMESTAMP(mined_time)*1000 from ud_transaction_recods_vout  where CHAR_LENGTH(address)>10  and `value`>500 and mined_time>DATE_FORMAT(Now(),'%Y-%m-%d') order by mined_time desc  "
        big_order_query = "select * from (select address,value,DATE_FORMAT(mined_time,   '%Y-%m-%d %H:%i:%S'),has_vin,UNIX_TIMESTAMP(mined_time)*1000,mined_time from ud_transaction_recods_vout  where `value`>500 and `has_trans`=0 and (mined_day=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -24 HOUR),  '%Y-%m-%d') or mined_day=DATE_FORMAT(NOW(),   '%Y-%m-%d')) order by mined_time desc ) a where a.mined_time>DATE_ADD(NOW(),INTERVAL -24 HOUR)"

        res = db.session.execute(big_order_query)
        row_list = res.fetchall()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print e

    order_list = []
    for index in range(len(row_list)):
        list = []
        list.append(row_list[index][0])
        list.append(row_list[index][1])
        list.append(row_list[index][2])
        list.append(row_list[index][3])
        list.append(row_list[index][4])
        order_list.append(list)

    return order_list