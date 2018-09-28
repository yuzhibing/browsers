import datetime,time
import schedule
from rawtransaction_task import *
from addres_count_task import *
from trans_address_task import *
from crawl_ulord_price_task import *
from trans_block_task import *

def block_job():
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("run crawl_ulord job:", datetime.datetime.now())
    crawl_ulord()
    crawl_price_coin()
    print("run block_check job:", datetime.datetime.now())
    rsync_block()
    print("run address_count job:", datetime.datetime.now())
    address_count_job()
    print("run trans_address_count job:", datetime.datetime.now())
    tran_address_job('')
    print("run trans_block_update job:", datetime.datetime.now())
    trans_block_update()







if __name__ == '__main__':
    print('job run...')
    schedule.every(10).minutes.do(block_job)
    while True:
        beginTime = datetime.datetime.now()
        print('block_job run...', beginTime)
        schedule.run_pending()
        time.sleep(60)