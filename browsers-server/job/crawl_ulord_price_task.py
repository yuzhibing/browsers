# -*- coding: utf-8 -*-
"""
@Author: Shucheng Zhang(050511)
"""

import requests,os,time,datetime,json
import sys

from lxml import etree
from job_create_db import *

reload(sys)
sys.setdefaultencoding('utf8')


def crawl_price_coin():
    try:
        sp = time.time()
        st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sp))
        etl_time = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")
        target_url = "https://www.aicoin.net.cn/api/second/global_custom?symbol=kucoinuteth&list_flag=2"
        headers = {"Accept": "*/*",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Accept-Language": "zh-CN,zh;q=0.9",
                   "Connection": "keep-alive",
                   "Cookie": "_ga=GA1.3.56640674.1537171331; Hm_lvt_3c606e4c5bc6e9ff490f59ae4106beb4=1537171331,1537171419,1537171773; acw_tc=784c10e115378666792501369ed44e4f9808ab78a3b64d96ac3260bc4abf69; _gid=GA1.3.1697212968.1537866685; Hm_lpvt_3c606e4c5bc6e9ff490f59ae4106beb4=1537868855; _gat_gtag_UA_108140256_2=1; XSRF-TOKEN=eyJpdiI6Im1SYVRGVHB6WWUwSURpeGFYemNFYUE9PSIsInZhbHVlIjoiaXdMbmtoNWh2MWNjYmdGRVRnY1lFVytpQ2VwZllPZ3RwZHdqYlJyQWdUVHF5anJQc1F2NElXanZwN2tkenNod2RxVkpqN3pDK2EzaCtNTjd5dkI0eVE9PSIsIm1hYyI6ImM3YzgzMThmYzAyMTY3ZjhkNzA0ZWI3OWQzZjg4MmFlMzJjOWMyYzI0NzNlNjNhZGEyNDNjYWIwNDMxOGZhOWQifQ%3D%3D; aicoin_session=eyJpdiI6Im1TZ1hmMzcwTmUwNXNkQ3UyRDNEWWc9PSIsInZhbHVlIjoiaXgybjJ0cDg3MEFlUWZiRjQ1UGczQjVTdzlodjlKZW1GeG8wK3NsbXo4XC9CTDFLcU83T08xYVNJa2xMYkliSVNHcVhSUW5vbm1HWUJXbTVXZ21GVGFRPT0iLCJtYWMiOiJlYmI0YmU4MTFhYTgwMTVkNmUzODg1YmE5Yjc3M2VlODNjNzJjOTQwYThkNjE1ZTMzMzU0NTY4MDU1NTRiYzg0In0%3D",
                   "Host": "www.aicoin.net.cn",
                   "Referer": "https://www.aicoin.net.cn/",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        r = requests.get(target_url, headers=headers)
        d = r.text

        data = json.loads(d)
        price_data_list = data["quotes"]
        price_info_list = []

        for price_data in price_data_list:
            price = price_data["last_curr"]
            currency_base = price_data["currency_base"]
            if currency_base == "lbanketh":
                currency_name = "UT/ETH(LBank)"
            elif currency_base == "kucoineth":
                currency_name = "UT/ETH(Kucoin)"
            elif currency_base == "kucoinbtc":
                currency_name = "UT/BTC(Kucoin)"
            else:
                currency_name = "UT/ETH(BBX)"
            price_info = (currency_name, price, etl_time)
            price_info_list.append(price_info)

            sql = "insert into ud_price (create_time,price,platform) VALUES (DATE_FORMAT(NOW(),   '%%Y-%%m-%%d %%H:%%i'),'%s','%s')" % \
                  (price, currency_name)
            print sql
            res = db.session.execute(sql)

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(e)

def crawl_ulord():
    try :

        #获取当前时间
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        time_now = int(time.time())
        #转换成localtime
        time_local = time.localtime(time_now)
        #转换成新的时间格式(2016-05-09 18:59:20)
        etl_time = time.strftime('"%Y-%m-%d %H:%M:%S"',time_local)
        url = "http://www.topbtc.one/"
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "PHPSESSID=jna61tcaorgat5o41nd08d6i46; _ga=GA1.2.1660271731.1529467228; _gid=GA1.2.1811285768.1529467228; _gat=1; SERVERID=90f486e728e39041f7d76ebd13f977d3|1529467248|1529467225",
        "Host": "www.topbtc.one",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
        r = requests.get(url,headers=headers)
        d = r.text
        html = etree.HTML(d)
        coinname = html.xpath("//div[@id='ETHMarket']/table/tbody/tr/td[2]/text()")
        coinname = ["".join(name.split()) for name in coinname]

        price_list = html.xpath("//div[@id='ETHMarket']/table/tbody/tr/td[3]/span/text()")
        price_list = [price.replace("/¥","")for price in price_list]

        info = (etl_time,price_list)
        dict_list = dict(zip(coinname,price_list))

        for name in coinname:
            if "(UT/ETH)" in name:
                target_key = name
        price = dict_list[target_key]


        # 创建连接

        sql = "insert into ud_price (create_time,price,platform) VALUES (DATE_FORMAT(NOW(),   '%%Y-%%m-%%d %%H:%%i'),'%s','%s')" % \
              (price,'topbtc')
        print sql

        res = db.session.execute(sql)
        db.session.commit()
    except Exception as e:
      db.session.rollback()
      print(e)



