from flask import Flask
from create_db import *

def trans_speed(f):
    trans_query = ""
    if f=="hour":
        trans_query = "select a.timestamp,a.day_time,a.trans_num,a.total_block,a.m_min,(a.total_block_size/a.total_block) avg_block_size,(a.m_min*a.trans_num) speed from (select timestamp, FROM_UNIXTIME(timestamp,'%Y-%m-%d %H') day_time, sum(total_trans) trans_num, count(1) total_block, 0.4 m_min, sum(size) total_block_size from ud_block where FROM_UNIXTIME(timestamp,'%Y-%m-%d')>=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -1 DAY),'%Y-%m-%d') and FROM_UNIXTIME(timestamp,'%Y-%m-%d') <=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -1 DAY),'%Y-%m-%d')  group by FROM_UNIXTIME(timestamp,'%Y-%m-%d %H') ) a"
    elif f=="day":
        trans_query = "select a.timestamp,a.day_time,a.trans_num,a.total_block,a.m_min,(a.total_block_size/a.total_block) avg_block_size,(a.m_min*a.trans_num) speed from (select timestamp, FROM_UNIXTIME(timestamp,'%Y-%m-%d %H') day_time, sum(total_trans) trans_num, count(1) total_block, 0.4 m_min, sum(size) total_block_size from ud_block where FROM_UNIXTIME(timestamp,'%Y-%m-%d')>=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -30 DAY),'%Y-%m-%d') and FROM_UNIXTIME(timestamp,'%Y-%m-%d') <=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -1 DAY),'%Y-%m-%d')  group by FROM_UNIXTIME(timestamp,'%Y-%m-%d') ) a"
    elif f=="week":
        trans_query = "select a.timestamp,a.day_time,a.trans_num,a.total_block,a.m_min,(a.total_block_size/a.total_block) avg_block_size,(a.m_min*a.trans_num) speed,FROM_UNIXTIME(a.timestamp,'%W') w from (select timestamp, FROM_UNIXTIME(timestamp,'%Y-%m-%d %H') day_time, sum(total_trans) trans_num, count(1) total_block, 0.4 m_min, sum(size) total_block_size from ud_block where FROM_UNIXTIME(timestamp,'%Y-%m-%d')>=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -7 DAY),'%Y-%m-%d') and FROM_UNIXTIME(timestamp,'%Y-%m-%d') <=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -1 DAY),'%Y-%m-%d')  group by FROM_UNIXTIME(timestamp,'%Y-%m-%d') ) a "
    elif f=="month":
        trans_query = "select a.timestamp,a.day_time,a.trans_num,a.total_block,a.m_min,(a.total_block_size/a.total_block) avg_block_size,(a.m_min*a.trans_num) speed from (select timestamp, FROM_UNIXTIME(timestamp,'%Y-%m-%d %H') day_time, sum(total_trans) trans_num, count(1) total_block, 0.4 m_min, sum(size) total_block_size from ud_block where FROM_UNIXTIME(timestamp,'%Y-%m-%d')>=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -12 month),'%Y-%m-%d') and FROM_UNIXTIME(timestamp,'%Y-%m-%d') <=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -1 DAY),'%Y-%m-%d')  group by FROM_UNIXTIME(timestamp,'%Y-%m') ) a"

    row_list = []
    try :

        res = db.session.execute( trans_query)
        row_list = res.fetchall()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print e

    trans_list = []
    for index in range(len(row_list)):
        list = []
        if f=="week":
            list.append(row_list[index][7])
        else:
            list.append(row_list[index][0])
        list.append(str(row_list[index][1]))
        list.append(str(row_list[index][2]))
        list.append(str(row_list[index][3]))
        list.append(str(row_list[index][4]))
        list.append(str(row_list[index][5]))
        list.append(str(row_list[index][6]))
        trans_list.append(list)


    return trans_list