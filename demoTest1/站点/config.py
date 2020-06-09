import datetime
import json
import time

import pymysql
import requests

from 沪遇优选.最新代码.snow_id2 import IdWorker

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'http://2382.bd.aiyichuan.com/',
    'Cookie': 'snapid=af3ed7f620841dd3b69ac6a80c8188e6; qsy_2382_053user_id=DPLupJYbzIm9bHbjt8E_ebuKo77; qsy_2382_054user_id=FLGc7zlHbEnLUn8ltoG7eWc01jl; PHPSESSID=pujei4d9jqud8onomdiq5daekn; lat=30.2084; lng=120.21201; loc_time=1588068386; site_id=1; SERVERID=7a86cd5e7bf8aadcae90b9f540561537|1588071992|1588071048'
}

host = '192.168.1.52'
user = 'jpss'
passwd = 'Jpss541018!'
database = 'hbsitedb'

goods_category_id_dict = {
    # 美食对应的门店一级和二级类目id
    '29': [1234823381360816128, 1235024460169015296],

    # 亲子
    '27': [1234825032956096512, 1235026545765707776],

    # 丽人
    '9': [1234824686405922816, 1235025522099679232],

    # 生活
    '36': [1234825580560232448, 1235028555554549760]
}

# 门店类目id
shop_category_id_dict = {
    # 美食对应的门店一级和二级类目id
    '29': [1235028620859863040, 1235029134800515072],

    # 亲子
    '27': [1235028711444246528, 1235029696476540928],

    # 丽人
    '9': [1235028682117672960, 1235029542520418304],

    # 生活
    '36': [1235028735859290112, 1235029877611753472]
}

# 门店商圈对应的id
shop_center_id_dict = {'2': ['静安区', 1255391527249780736], '4': ['徐汇区', 1255391527333666816], '3': ['长宁区', 1255391527375609856], '5': ['杨浦区', 1255391527459495936], '6': ['黄浦区', 1255391527543382016], '7': ['虹口区', 1255391527627268096], '8': ['闵行区', 1255391527711154176], '9': ['宝山区', 1255391527753097216], '10': ['浦东新区', 1255391527836983296], '11': ['普陀区', 1255391527878926336], '13': ['嘉定区', 1255391527962812416], '14': ['奉贤区', 1255391528046698496], '15': ['金山区', 1255391528088641536], '16': ['青浦区', 1255391528130584576], '17': ['崇明区', 1255391528214470656], '18': ['松江区', 1255391528256413696]}


# 获取站点id
def get_site_id_by_name(site_name):
    city = '上海市'

    sql = 'select s.id,a.area_name,s.name,a.area_code from site s left join area a on a.area_code =s.code where s.deleted =0 and a.area_type =2 and a.area_name like \"' + city + '\"'
    conn = pymysql.connect(host=host,
                           user=user,
                           passwd=passwd,
                           db=database)
    cursor = conn.cursor()
    print('sql=', sql)
    cursor.execute(sql)
    result = cursor.fetchone()
    site_id = result[0]
    cursor.close()
    conn.close()
    return site_id


def get_shop_center():
    url = 'http://2382.bd.aiyichuan.com/wap/Act/b2c_ajax?type=cat&cat_id=29&order=back&cbd_id=2&b2c_p_cat_id=&page=1'
    response = requests.get(url, headers=headers)
    text = response.content.decode()
    json_text = json.loads(text)
    data = json_text['data']
    cbd = data['cbd']

    get_shop_center_dict = {}
    for i in range(len(cbd)):
        temp_d = cbd[i]

        id = temp_d['id']
        name = temp_d['name']
        get_shop_center_dict[str(id)] = name
    return get_shop_center_dict


def insert_data(sql, args):
    try:
        conn = pymysql.connect(host=host,
                               user=user,
                               passwd=passwd,
                               db=database)
        cursor = conn.cursor()
        # args 需是元组列表
        print('sql=', sql, ';args=', args)
        cursor.executemany(sql, args)
        conn.commit()
    except Exception as e:
        print('Error msg: ' + e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def shop_center_sql(get_shop_center_dict, site_id):
    args_tuple_list = []
    for index in get_shop_center_dict:
        da_list = []
        id = IdWorker(1, 2, 0).get_id()
        time.sleep(0.01)
        name = get_shop_center_dict[str(index)]
        deleted = 0
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        modify_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        version = 0

        da_list.append(id)
        da_list.append(site_id)
        da_list.append(name)
        da_list.append(deleted)
        da_list.append(create_time)
        da_list.append(modify_time)
        da_list.append(version)
        t_data = tuple(da_list)
        args_tuple_list.append(t_data)
        sql = 'insert into shop_center_define (id,site_id,name,deleted,create_time,modify_time,version) values (%s,%s, %s, %s, %s, %s, %s)'
    return sql, args_tuple_list


def get_center_result(site_id):
    result_dict = {}
    sql = 'select name,id from shop_center_define where deleted =0 and site_id =' + str(site_id)
    conn = pymysql.connect(host=host,
                           user=user,
                           passwd=passwd,
                           db=database)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        result_dict[data[0]]=data[1]
    cursor.close()
    conn.close()
    return result_dict





if __name__ == '__main__':
    # city = '上海市'
    # site_id = get_site_id_by_name(city)
    # print(site_id)

    site_id = 11001
    get_shop_center_dict = get_shop_center()

    print('get_shop_center_dict=', get_shop_center_dict)



    result_dict = get_center_result(site_id)
    if len(result_dict) == 0:
        sql, args_tuple_list = shop_center_sql(get_shop_center_dict, site_id)
        insert_data(sql, args_tuple_list)

        result_dict = get_center_result(site_id)
    print('result_dict=',result_dict)


    new_dict={}
    for bcd_id in get_shop_center_dict:
        name=get_shop_center_dict[bcd_id]
        t_id=result_dict[name]

        t_list=[]
        t_list.append(name)
        t_list.append(t_id)
        new_dict[bcd_id]=t_list

    print(new_dict)



