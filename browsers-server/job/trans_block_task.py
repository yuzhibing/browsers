#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
from job_create_db import *
import traceback

###账户数量统计


def trans_block_count(height):
  try:


      trans_query_sql = "select count(1) from ud_transaction_recods_vout where height=%s and `has_trans`=0" % \
                          (height)

      res = db.session.execute(trans_query_sql)
      trans_count = res.fetchone()


      trans_address_update_sql = "update ud_block set total_trans=%s  where height=%s" % \
                                     (trans_count[0],height)
      db.session.execute(trans_address_update_sql)
      db.session.commit()
  except Exception as e:
      db.session.rollback()
      traceback.print_exc()






def trans_block_update():
    try:

        trans_query_sql = "select height from ud_block where total_trans is null"

        res = db.session.execute(trans_query_sql)
        height_list = res.fetchall()
        db.session.commit()
        for index in range(len(height_list)):
            trans_block_count(height_list[index][0])
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()


