#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
from job_create_db import *

###


def address_count(address):
    try:
            update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


            vout_query_sql ="select  sum(value) as Total_Received, count(*) as trans_no, address, (select  sum(value) from ud_transaction_recods_vout where address =vout.address and has_vin=0) as Final_Balance, (select  sum(value) from ud_transaction_recods_vout where address =vout.address and has_vin=1 ) as Total_Sent, max(vout.mined_time)  from ud_transaction_recods_vout  vout  where  address='%s'  group by address" % \
                            (address)
            print vout_query_sql
            res = db.session.execute(vout_query_sql)
            address_value = res.fetchall()

            Total_Received=address_value[0][0]
            if Total_Received == None:
                Total_Received = 0

            trans_no = address_value[0][1]
            if trans_no == None:
                trans_no = 0

            Final_Balance = address_value[0][3]
            if Final_Balance == None:
                Final_Balance = 0

            Total_Sent=address_value[0][4]
            if Total_Sent == None:
                Total_Sent=0

            address_detail_query_sql = "select * from ud_address_details where address='%s'" % \
                                       (address)
            res = db.session.execute(address_detail_query_sql)
            addr = res.fetchone()
            if addr == None:

                address_detail_insert_sql = "insert into ud_address_details(Address , Total_Received, Total_Sent, Final_Balance, update_time, trans_no) VALUES('%s','%s','%s','%s',DATE_FORMAT('%s','%%Y-%%m-%%d'),'%s')" % \
                                        (address , Total_Received, Total_Sent, Final_Balance, update_time, trans_no)
                db.session.execute(address_detail_insert_sql)
            else :
                address_detail_update_sql = "update ud_address_details set  Total_Received='%s', Total_Sent='%s', Final_Balance='%s', update_time=DATE_FORMAT('%s','%%Y-%%m-%%d'), trans_no='%s'  where address='%s'" % \
                                            (Total_Received, Total_Sent, Final_Balance, update_time, trans_no,address)
                db.session.execute(address_detail_update_sql)

            address_delete_sql = "delete from ud_transaction_recods_address where address='%s'" % \
                                    (address)
            db.session.execute(address_delete_sql)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        print str(e)
    finally:
        print('finally count_address',address,update_time)

def query_address():
    address_query_sql = "select address  from ud_transaction_recods_address group by address"
    res = db.session.execute(address_query_sql)
    addressList = res.fetchall()
    return addressList

def address_count_job():
    try:
        addressList = query_address()
        for index in range(len(addressList)):
            address=addressList[index][0]
            address_count(address)

    except Exception as e:
        db.rollback()
        print str(e)
    finally:
        print('finally count_address')





