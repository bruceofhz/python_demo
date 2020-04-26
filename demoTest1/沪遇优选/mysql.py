import datetime

import pymysql

host = '192.168.1.52'
user = 'jpss'
passwd = 'Jpss541018!'
database = 'hbsitedb-test'


def select_data(sql):
    result = []
    try:
        db = pymysql.connect(host=host,
                             user=user,
                             passwd=passwd,
                             db=database)
        cursor = db.cursor()
        cursor.execute(sql)
        alldata = cursor.fetchall()

        for rec in alldata:
            # 注意，我这里只是把查询出来的第一列数据保存到结果中了,如果是多列的话，稍微修改下就ok了
            result.append(rec[0])

    except Exception as e:
        print('Error msg: ' + e)
    finally:
        cursor.close()
        db.close()
        return result


def insert_data(sql, args):
    try:
        conn = pymysql.connect(host=host,
                               user=user,
                               passwd=passwd,
                               db=database)

        print('sql=' + sql)
        print(args)
        cursor = conn.cursor()
        cursor.execute(sql, args)

        conn.commit()

    except Exception as e:
        print('Error msg: ' + e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    sql = 'select * from order_refund where deleted =0 '

    list = []

    id = 11232316
    site_id = None
    cust_id = 1236271
    t_name = '吴'
    mobile = '15000257840'
    business_name = 'cesg'
    business_nun = 2
    province = '北京市'
    city = '北京市'
    district = '东城区'
    address = '北路'
    remark = ''
    status = 1
    deleted = 0
    create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modify_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    version = 0

    list.append(id)
    list.append(site_id)
    list.append(cust_id)
    list.append(t_name)
    list.append(mobile)
    list.append(business_name)
    list.append(business_nun)
    list.append(province)
    list.append(city)
    list.append(district)
    list.append(address)
    list.append(remark)
    list.append(status)
    list.append(deleted)
    list.append(create_time)
    list.append(modify_time)
    list.append(version)

    a = tuple(list)

    insert_sql = "insert into bus_intention (id,site_id,cust_id,name,mobile,business_name,business_num,province,city,district,address,remark,status,deleted,create_time,modify_time,version) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # insert_sql = 'insert into bus_intention (id,site_id,cust_id,name,mobile,business_name,business_num,province,city,district,address,remark,status,deleted,create_time,modify_time,version) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    # result = select_data(sql)
    # print(result)
    #
    insert_data(insert_sql, a)
