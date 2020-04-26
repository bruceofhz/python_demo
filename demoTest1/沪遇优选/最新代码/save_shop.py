import csv
import datetime

import pymysql

from 沪遇优选.雪花id.snow_id import MySnow




class save_shop_class:
    def __init__(self, host, user, passwd, database,shop_center_id_dict,site_id,file_path):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.shop_center_id_dict = shop_center_id_dict
        self.site_id = site_id
        self.file_path = file_path


    def insert_data(self,sql, args):
        try:
            conn = pymysql.connect(host=self.host,
                                   user=self.user,
                                   passwd=self.passwd,
                                   db=self.database)
            cursor = conn.cursor()
            # args 需是元组列表
            print('sql=' + sql)
            print(args)
            cursor.executemany(sql, args)
            conn.commit()
        except Exception as e:
            print('Error msg: ' + e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


    # 将list切割多个
    def split_list(self,data_list, max_size, spilt_data_list):
        if len(data_list) <= max_size:
            spilt_data_list.append(data_list)
            return spilt_data_list
        else:
            spilt_data_list.append(data_list[:max_size])
            return save_shop_class.split_list(self,data_list[max_size:], max_size, spilt_data_list)



    def get_insert_shop_sql(self,list1, site_id):
        shop_args_tuple_list = []

        for shop_data in list1:
            da_list = []
            shop_name=shop_data[1]
            shop_address=shop_data[2]
            shop_mobile=shop_data[3]
            shop_hours=shop_data[4]
            lon=shop_data[5]
            lat=shop_data[6]

            origin_shop_id = shop_data[0]
            # id = 1
            first_category =shop_data[7]
            second_category = shop_data[8]
            shop_center_id = shop_data[9]
            tenant_id = 10000
            shop_mode = 1
            name = shop_name
            logo = None
            charge_name = '李明'
            charge_mobile = '17707138916'
            country = '中国'
            country_code = '000000'
            province = '上海市'
            province_code = '310000'
            city = '上海市'
            city_code = '310100'
            district = '黄浦区'
            district_code = '310101'
            street = None
            address = shop_address
            # lon = 0
            # lat = 0
            radiation_range = 1000
            tel = shop_mobile[0:12]
            intro = '暂无简介'
            imgs = ''
            buss_type = 2
            buss_time = shop_hours
            supp_fac = '1,3'
            d = datetime.datetime.now() + datetime.timedelta(30)
            coop_start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            coop_end_time = d.strftime("%Y-%m-%d %H:%M:%S")
            status = 1

            deleted = 0
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            modify_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            version = 0

            da_list.append(origin_shop_id)
            da_list.append(site_id)
            da_list.append(first_category)
            da_list.append(second_category)
            da_list.append(shop_center_id)
            da_list.append(tenant_id)
            da_list.append(shop_mode)
            da_list.append(name)
            da_list.append(logo)
            da_list.append(charge_name)
            da_list.append(charge_mobile)
            da_list.append(country)
            da_list.append(country_code)
            da_list.append(province)
            da_list.append(province_code)
            da_list.append(city)
            da_list.append(city_code)
            da_list.append(district)
            da_list.append(district_code)
            da_list.append(street)
            da_list.append(address)
            da_list.append(lon)
            da_list.append(lat)
            da_list.append(radiation_range)
            da_list.append(tel)
            da_list.append(intro)
            da_list.append(imgs)
            da_list.append(buss_type)
            da_list.append(buss_time)
            da_list.append(supp_fac)
            da_list.append(coop_start_time)
            da_list.append(coop_end_time)
            da_list.append(status)

            da_list.append(deleted)
            da_list.append(create_time)
            da_list.append(modify_time)
            da_list.append(version)

            t_data = tuple(da_list)
            shop_args_tuple_list.append(t_data)

            shop_sql = 'insert into shop (origin_shop_id,site_id,first_category,second_category,shop_center_id,tenant_id,shop_mode,name,logo,charge_name,charge_mobile,country,country_code,province,province_code,city,city_code,district,district_code,street,address,lon,lat,radiation_range,tel,intro,imgs,buss_type,buss_time,supp_fac,coop_start_time,coop_end_time,status,deleted,create_time,modify_time,version) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        return shop_sql, shop_args_tuple_list


    def save_shop_data(self):
        site_id = self.site_id
        file_path = self.file_path
        data_list = []
        # 分批数量，每批次150个商品
        spilt_data_list = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for r in reader:
                data_list.append(r)
        data_list = data_list[1:]
        # 每批次最大数量
        max_size = 100
        spilt_data_list = save_shop_class.split_list(self,data_list, max_size, spilt_data_list)
        # 分批插入spu，匹配门店类目和门店商圈
        for list1 in spilt_data_list:
            # 保存shop
            shop_sql, shop_args_tuple_list = save_shop_class.get_insert_shop_sql(self,list1, site_id)
            save_shop_class.insert_data(self,shop_sql, shop_args_tuple_list)


















