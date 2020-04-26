import pymysql

file_path = 'D:\\project\\python\\沪遇优选商品\\爬取商品.csv'

data_list = []

# with open(file_path, 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for r in reader:
#         data_list.append(r)
#
#     print(data_list)


str_1 = "['http://q6.img.aiyichuan.com/urm_huodong/20200422/1587523656621.jpg?imageView2/1/w/750/h/750', 'http://q6.img.aiyichuan.com/urm_huodong/20200422/1587523657768.jpg?imageView2/1/w/750/h/750', 'http://q6.img.aiyichuan.com/urm_huodong/20200422/1587523659231.jpg?imageView2/1/w/750/h/750', 'http://q6.img.aiyichuan.com/urm_huodong/20200422/1587523660134.jpg?imageView2/1/w/750/h/750', 'http://q6.img.aiyichuan.com/urm_huodong/20200422/1587523660965.jpg?imageView2/1/w/750/h/750', 'http://q6.img.aiyichuan.com/urm_huodong/20200422/1587523662173.jpg?imageView2/1/w/750/h/750', 'http://q6.img.aiyichuan.com/urm_huodong/20200422/1587523662856.jpg?imageView2/1/w/750/h/750']"


# args_one_data = str((%s,) * 37)
# 
# print(args_one_data)
#
# str_list = str_2.split(',')
# print(str_list)
#
# print('###############')
# print(str_list[0])
# print(str_list[1])
# print(str_list[2])

# a = ','.join(str_list)
# print(a)
# a.replace('\'', '')
# print(type(a))
# print(a)


def f(x):
    return x * x


# data_map=map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(data_map))

host = '192.168.1.52'
user = 'jpss'
passwd = 'Jpss541018!'
database = 'hbsitedb'
# data = {'id':['A','B','C','C','C','A','B','C','A'],'age':[18,20,14,10,50,14,65,14,98]}
data = [
    [1213, '111'],
    [1214, '222'],
    [1214, '222'],
    [1215, '333']
]



list_1=[1213, '111']
list_2= [1214, 1214,'222']
list_3= [1214, '222']
list_4=[1215, '555']



total_list={}
total_list['1']=list_1
total_list['3']=list_2
total_list['5']=list_3
total_list['7']=list_4

site_id='11000'
# sql="select id,origin_shop_id from shop where deleted =0 and  create_time >'2020-04-25 10:56:58' and site_id ="+site_id
# print(sql)


def deal_with_shop_id_mapping():
    site_id = '11000'
    shop_id_mapping={}
    sql="select id,origin_shop_id from shop where deleted =0 and  create_time >'2020-04-25 10:56:58' and site_id ="+str(site_id)
    conn = pymysql.connect(host=host,
                           user=user,
                           passwd=passwd,
                           db=database)
    cursor = conn.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    for data in result:
        shop_id_mapping[data[0]]=data[1]

    cursor.close()
    conn.close()
    return shop_id_mapping


if __name__ == '__main__':
    shop_id_mapping=deal_with_shop_id_mapping()
    print(type(shop_id_mapping))
    print(shop_id_mapping)

# print('total_list1=', total_list['1'],'total_list2=', total_list['3'])

# print(data)
#
#
#
#
# data_1=data[0]
# print(data_1)
# print(data_1[0])

# snow=MySnow(10000)
# print(snow.get_id())


# print(data.index(1))
