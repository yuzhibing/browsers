#!/usr/bin/python
# -*- coding: UTF-8 -*-

from json import dumps, loads
from requests import request
import time
from job_create_db import *
from config import *


url = ULORD_IP
auth=(ULORD_USER, ULORD_PASSWORD)



def rsync_block():
    endHeight = load_height()

    max_height_query = "select max(HEIGHT) from ud_block"
    result = db.session.execute(max_height_query)
    max_height = result.fetchone()

    if max_height[0] != None :
        max_height=max_height[0]+1
    else:
        max_height = 1
    count = 0
    try:
        while True:
            height =max_height+count
            print('=================',height)
            block_load(height)


            update_sql = "UPDATE ud_transaction_recods_vout AS a1 INNER JOIN (SELECT * FROM ud_transaction_recods_vin WHERE vin_txid is not null and height='%s') AS a2 SET a1.has_vin = 1 where a1.txid = a2.vin_txid and a1.n=a2.vout" % \
                         (height)
            db.session.execute(update_sql)

            #has_trans 0交易；1挖矿奖励；2找零；
            update_vout_trans_sql = "UPDATE ud_transaction_recods_vout AS a1  INNER JOIN (select distinct vout.txid,vout.address from ud_transaction_recods_vout vout left join  ud_transaction_recods_vin vin on vout.txid=vin.txid left join ud_transaction_recods_vout vout2 on vout2.txid=vin.vin_txid and vin.vout=vout2.n  where  vout.height='%s'  and vout.address=vout2.address ) AS a2 SET a1.`has_trans`=2 where a1.txid=a2.TXID and a1.address=a2.address" % \
                                    (height)
            db.session.execute(update_vout_trans_sql)
            db.session.commit()

            #找零地址实际交易金额
           # trans_2_query = ""

            if height == endHeight:
                break;
            else:
                count = count+1
    except Exception as e:
        print('error',e)

def save_transaction(txList,ud_blockid):
    for index in range(len(txList)):
        tx = txList[index]
        payload = dumps({"method": 'getrawtransaction', "params": [tx, 1]})
        response = request("POST", url, data=payload, auth=auth)

        res = loads(response.text)
        HEIGHT = res['result']['height']
        TX_ID = res['result']['txid']
        confirmations = res['result']['confirmations']
        time = res['result']['time']
        blocktime = res['result']['blocktime']
        version = res['result']['version']
        fees = 0

        insert_ud_transaction_records_sql = "INSERT INTO ud_transaction_records(HEIGHT, TX_ID , confirmations , time , blocktime , version , fees , ud_blockid ) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                                            (HEIGHT,TX_ID, confirmations, time, blocktime, version, fees, ud_blockid)
        result = db.session.execute(insert_ud_transaction_records_sql)

        ud_transaction_recordsid = result.lastrowid
        mined_time = timestamp_to_date(time)
        ###vout
        vout = res['result']['vout']

        ##挖矿奖励
        coinbase = ""
        has_trans = 0
        try:
            coinbase = res['result']['vin'][0]['coinbase']
            has_trans = 1
        except Exception as e:
            coinbase = ""

        for index in range(len(vout)):
            value = vout[index]['value']
            n = vout[index]['n']
            vout_type = vout[index]['scriptPubKey']['type']
            address = vout[index]['scriptPubKey']['addresses'][0]



            insert_ud_transaction_recods_vout_sql = "INSERT INTO ud_transaction_recods_vout(value, n , txid , ud_transaction_recordsid,type,address,mined_time,coinbase,height,has_trans,has_vin,mined_day,trans_value) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s',DATE_FORMAT('%s','%%Y-%%m-%%d'),'%s')" % \
                                                (value, n, TX_ID, ud_transaction_recordsid,vout_type,address,mined_time,coinbase,HEIGHT,has_trans,0,mined_time,value)
            result = db.session.execute(insert_ud_transaction_recods_vout_sql)
            vout_id = result.lastrowid
            try:

                #####vout address
                if vout_type == 'pubkeyhash':
                    addresses = vout[index]['scriptPubKey']['addresses']
                    for index in range(len(addresses)):
                        addr = addresses[index]
                        insert_ud_transaction_recods_address_sql = "INSERT INTO ud_transaction_recods_address(address,ud_transaction_recods_voutid,mined_time) VALUES ('%s', '%s','%s')" % \
                                                                (addr, vout_id,mined_time)

                        db.session.execute(insert_ud_transaction_recods_address_sql)
                else :
                    print('nonstandard',TX_ID)
            except Exception as e:
                print("",e)
        #####vin
        vin = res['result']['vin']

        if len(vin[0]) > 2 :
            for index in range(len(vin)):
                vin_txid = vin[index]['txid']
                vout_index = vin[index]['vout']
                insert_ud_transaction_recods_vin_sql = "INSERT INTO ud_transaction_recods_vin(txid, vout , vin_txid , ud_transaction_recordsid,height) VALUES ('%s', '%s', '%s', '%s', '%s')" % \
                                                        (TX_ID, vout_index, vin_txid, ud_transaction_recordsid,HEIGHT)
                db.session.execute(insert_ud_transaction_recods_vin_sql)

        else :
            coinbase = vin[0]['coinbase']
            insert_ud_transaction_recods_vin_sql = "INSERT INTO ud_transaction_recods_vin(txid , coinbase , ud_transaction_recordsid,height) VALUES ('%s', '%s', '%s', '%s')" % \
                                                   (TX_ID, coinbase, ud_transaction_recordsid,HEIGHT)
            db.session.execute(insert_ud_transaction_recods_vin_sql)

def block_load(height):
    try:

        ub_block_query_sql = "select height from ud_block where height = %s" % \
                             (height)
        result = db.session.execute(ub_block_query_sql)
        block = result.fetchone()

        txList = []
        if block == None:


            payload = dumps({"method": 'getblockhash', "params": [height]})
            response = request("POST", url, data=payload, auth=auth)
            res = loads(response.text)
            blockHash =  res['result']

            #
            payload = dumps({"method": 'getblock', "params": [blockHash]})
            response = request("POST", url, data=payload, auth=auth)
            res = loads(response.text)

            ####
            height = res['result']['height']
            size = res['result']['size']
            bits = res['result']['bits']
            difficulty = res['result']['difficulty']
            previous_block =res['result']['previousblockhash']
            next_block =res['result']['nextblockhash']
            timestamp =res['result']['time']
            transactions_number = len(res['result']['tx'])
            block_reward = 112.96602502
            if height > 57599:
                block_reward=165.377




            insert_sql = "INSERT INTO ud_block(height,mined_by,difficulty,transactions_number,timestamp,Size,Bits, Block_reward , Previous_Block , Next_Block , BlockHash) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                               (height, '', difficulty, transactions_number, timestamp, size, bits, block_reward,previous_block, next_block, blockHash)

            result = db.session.execute(insert_sql)
            ud_blockid = result.lastrowid

            for index in  range(len(res['result']['tx'])):
                txList.append(res['result']['tx'][index])
            save_transaction(txList,ud_blockid)

        else:
            print('已存在',height)

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print str(e)
    finally:
        print('finally')

def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


def load_height():
    payload = dumps({"method": 'getblockcount', "params": []})
    response = request("POST", url, data=payload, auth=auth)
    res = loads(response.text)
    endHeight = res['result']
    return endHeight

