# !/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime,time
import concurrent.futures,threading
from rawtransaction_task import *
from addres_count_task import *
from trans_address_task import  *
from job_create_db import *
from trans_block_task import *


def rsync_block(height) :
        print('====rsync_block############################====',threading.current_thread().getName(), height)
        block_load(height)

def rsync_address(address):
        print('====rsync_address############################====', threading.current_thread().getName(), address)
        address_count(address)
def update_vin_trans():
    address_query_sql = "select height from ud_block"
    res = db.session.execute(address_query_sql)
    heightList = res.fetchall()

    for d in range(len(heightList)):
        height = heightList[d][0]
        update_sql = "UPDATE ud_transaction_recods_vout AS a1 INNER JOIN (SELECT * FROM ud_transaction_recods_vin WHERE vin_txid is not null and height is not null and height='%s') AS a2 SET a1.has_vin = 1 where a1.txid = a2.vin_txid and a1.n=a2.vout" % \
                     (height)
        db.session.execute(update_sql)

        # has_trans 0交易；1挖矿奖励；2找零；
        update_vout_trans_sql = "UPDATE ud_transaction_recods_vout AS a1  INNER JOIN (select distinct vout.txid,vout.address from ud_transaction_recods_vout vout left join  ud_transaction_recods_vin vin on vout.txid=vin.txid left join ud_transaction_recods_vout vout2 on vout2.txid=vin.vin_txid and vin.vout=vout2.n  where  vout.height='%s'  and vout.address=vout2.address ) AS a2 SET a1.`has_trans`=2 where a1.txid=a2.TXID and a1.address=a2.address" % \
                                (height)
        db.session.execute(update_vout_trans_sql)

        if d % 1000 == 0 or (d + 1) == len(heightList):
            print("height", d, len(heightList))
            db.session.commit()
def block_thread():
        endHeight = load_height()
        # 线程池执行
        start_time_1 = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                futures = [executor.submit(rsync_block, item) for item in range(endHeight)]
                for future in concurrent.futures.as_completed(futures):
                        print('====block==========', future.result())
        print ("block Thread pool execution in " + str(time.time() - start_time_1), "seconds")



def address_thread():


                addressList = query_day_address()
                if len(addressList)>0:
                        start_time_1 = time.time()
                        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                                futures = [executor.submit(rsync_address, addressList[item][0]) for item in range(len(addressList))]
                                for future in concurrent.futures.as_completed(futures):
                                        print('====address==========', future.result())
                        print ("address Thread pool execution in " + str(time.time() - start_time_1), "seconds")

def query_day_address():

     address_query_sql = "select address from ud_transaction_recods_vout vout  group by address"
     res = db.session.execute(address_query_sql)
     addressList = res.fetchall()
     return addressList

def days(str1,str2):
    date1=datetime.datetime.strptime(str1[0:10],"%Y-%m-%d")
    date2=datetime.datetime.strptime(str2[0:10],"%Y-%m-%d")
    num=(date1-date2).days
    return num

def day_run():
        block_begin_time = "2018-05-22 23:59:59"
        curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #两个日期相隔天数
        day_num = days(curr_time,block_begin_time)
        #
        d1 = datetime.datetime.strptime(block_begin_time, '%Y-%m-%d %H:%M:%S')

        for d in range(0, day_num):
                curr_d = d1 + datetime.timedelta(d)
                tran_address_job(curr_d)

if __name__ == "__main__":
        block_thread()
        update_vin_trans()
        trans_block_update()
        address_thread()
        day_run()




