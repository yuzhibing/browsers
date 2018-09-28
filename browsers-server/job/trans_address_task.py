#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
from job_create_db import *
import traceback

###账户数量统计


def trans_address_count(curr_time):
  try:

      address_query_sql = "";
      if curr_time == '':
         address_query_sql = "select (select count(distinct address) from ud_address_details where `Final_Balance`>=10000) as gt10000,(select count(distinct address) from ud_address_details where `Final_Balance`>0) as gt0,(select count(distinct address) from ud_address_details) as address_num"
         curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      else:
        address_query_sql = "select  count(CASE WHEN a.`Final_Balance`>=10000 THEN 1 end) as gt10000,count(CASE WHEN a.`Final_Balance`>0 THEN 1 end) as gt0,count(distinct a.address)  as address_num from (select address,   sum(CASE WHEN has_vin=0 THEN value end) as Final_Balance from ud_transaction_recods_vout  vout  where vout.`mined_day`<=DATE_FORMAT('%s','%%Y-%%m-%%d') group by address) a" % \
                          (curr_time)
      print address_query_sql
      res = db.session.execute(address_query_sql)
      address_count = res.fetchone()

      gt10000_address = address_count[0]
      gt0_address = address_count[1]
      address_num = address_count[2]

      trans_address_query_sql = "select count(distinct address) from ud_transaction_recods_vout where mined_time>=DATE_ADD('%s',INTERVAL -7 DAY) and mined_time<DATE_ADD('%s',INTERVAL 0 DAY) and has_vin =1" % \
                                (curr_time,curr_time)
      res = db.session.execute(trans_address_query_sql)
      trans_address_num = res.fetchone()
      trans_num = trans_address_num[0]


      trans_address_query = "select * FROM ud_trans_address where create_date=DATE_FORMAT('%s','%%Y-%%m-%%d') " % \
                            (curr_time)
      res = db.session.execute(trans_address_query)
      trans_address = res.fetchone()
      if trans_address == None:
          trans_address_insert_sql = "insert into ud_trans_address(create_date , gt10000_address, gt0_address, trans_num, address_num ) VALUES(DATE_FORMAT('%s','%%Y-%%m-%%d'),'%s','%s','%s','%s')" % \
                                     (curr_time, gt10000_address, gt0_address, trans_num,address_num)
          db.session.execute(trans_address_insert_sql)
      else :
          trans_address_update_sql = "update ud_trans_address set gt10000_address='%s', gt0_address='%s', trans_num='%s', address_num='%s'  where create_date=DATE_FORMAT('%s','%%Y-%%m-%%d')" % \
                                     (gt10000_address, gt0_address, trans_num, address_num,curr_time)
          db.session.execute(trans_address_update_sql)

      db.session.commit()
  except Exception as e:
      db.session.rollback()
      traceback.print_exc()




def tran_address_job(update_time):
    #update_time = datetime.datetime.now().strftime('%Y-%m-%d')
    trans_address_count(update_time)



