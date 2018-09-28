from create_db import *


def query_address():
    row_list = []
    try:
        address_query = "select DATE_FORMAT(create_date,'%Y-%m-%d'),gt10000_address,gt0_address,trans_num,address_num from ud_trans_address where create_date>=DATE_FORMAT(DATE_ADD(NOW(),INTERVAL -90 DAY),'%Y-%m-%d') and create_date <=DATE_FORMAT(NOW(),'%Y-%m-%d') order by create_date asc"

        res = db.session.execute(address_query)
        row_list = res.fetchall()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print e

    all_address_list = []
    for index in range(len(row_list)):
        address_list = []
        address_list.append(row_list[index][0])
        address_list.append(row_list[index][1])
        address_list.append(row_list[index][2])
        address_list.append(row_list[index][3])
        address_list.append(row_list[index][4])
        all_address_list.append(address_list)

    return all_address_list