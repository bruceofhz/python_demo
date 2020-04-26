import csv
import datetime
import time

import pymysql

from 沪遇优选.雪花id.snow_id2 import IdWorker

host = '192.168.1.52'
user = 'jpss'
passwd = 'Jpss541018!'
database = 'hbsitedb'



class save_item_class:
    def __init__(self,host,user,passwd,database,site_id,file_path):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.database=database
        self.site_id=site_id
        self.file_path=file_path



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



    # sku的结算价，库存，分佣
    def get_insert_sku_sql(self,sku_list,spu_id_list):
        sku_args_tuple_list = []
        sku_id_list=[]

        for size,sku_data in enumerate(sku_list):
            # print('第', size, '个数字是:', sku_data)
            sku_data = sku_list[size]
            da_list = []

            # id = MySnow(dataID="10002").get_id()
            id = IdWorker(1, 2, 0).get_id()
            time.sleep(0.01)
            spu_id =spu_id_list[size]
            is_default = 1
            sku_no=None
            sku_name = sku_data[1]
            sku_cover = sku_data[9]
            spec_ids = ''
            spec_names = ''
            ori_price=sku_data[3]
            price=sku_data[4]
            settle_price=sku_data[3]

            #库存
            top_deduct_amount=10
            stock=sku_data[5]
            sale_num=2
            virtual_sale_num=0
            buy_limit_num=2
            sort_order=0

            deleted = 0
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            modify_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            version = 0

            da_list.append(id)
            da_list.append(spu_id)
            da_list.append(is_default)
            da_list.append(sku_no)
            da_list.append(sku_name)
            da_list.append(sku_cover)
            da_list.append(spec_ids)
            da_list.append(spec_names)
            da_list.append(ori_price)
            da_list.append(price)
            da_list.append(settle_price)
            da_list.append(top_deduct_amount)
            da_list.append(stock)
            da_list.append(sale_num)
            da_list.append(virtual_sale_num)
            da_list.append(buy_limit_num)
            da_list.append(sort_order)

            da_list.append(deleted)
            da_list.append(create_time)
            da_list.append(modify_time)
            da_list.append(version)

            sku_id_list.append(id)

            t_data = tuple(da_list)
            sku_args_tuple_list.append(t_data)

            sku_sql = 'insert into goods_sku (id,spu_id,is_default,sku_no,sku_name,sku_cover,spec_ids,spec_names,ori_price,price,settle_price,top_deduct_amount,stock,sale_num,virtual_sale_num,buy_limit_num,sort_order,deleted,create_time,modify_time,version) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        return sku_sql, sku_args_tuple_list,sku_id_list

    def get_insert_spu_sql(self,list1,site_id,spu_id_list,shop_id_mapping_dict):
        spu_args_tuple_list = []

        save_item_class.saveSpu(self,spu_args_tuple_list, list1,site_id,spu_id_list,shop_id_mapping_dict)

        goods_spu_sql = 'insert into goods_spu (id,third_flag,brand_id,site_id,first_category,second_category,tenant_id,shop_id,goods_mode,spu_name,cover,imgs,qr_code_img,poster_img,special_img,goods_guide_id ,goods_blob_id,sale_channel,sale_visible,sale_start_time,sale_end_time,show_start_count_down,show_sale_count_down,buy_need_attach,buy_attach_rule,service_mode,sale_mode,postage_type,postage,appoint_need_attach,appoint_attach_rule,appoint_advance_day,verify_mode,valid_period,use_start_time,use_end_time,refund_mode,refund_attach_rule, stock_type,adult_num,child_num,audit_status,goods_apply_id,spu_status,user_id,sort_order,deleted,create_time,modify_time,version) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        return goods_spu_sql, spu_args_tuple_list;

    def saveSpu(self,args_tuple_list, list1,site_id,spu_id_list,shop_id_mapping_dict):
        for data in list1:
            da_list = []


            id =  IdWorker(1, 2, 0).get_id()
            time.sleep(0.01)
            spu_id_list.append(id)

            third_flag = 0
            brand_id = None
            tenant_id = 10000
            goods_mode = 1
            # 商品二维码
            qr_code_img = ''
            special_img = None
            goods_blob_id = None
            sale_channel = 1
            sale_visible = 1
            show_start_count_down = 0
            show_sale_count_down = 0
            buy_need_attach = 0
            buy_attach_rule = ''
            service_mode = 1
            sale_mode = 1
            postage_type = 0
            postage = None
            appoint_need_attach = 0
            appoint_attach_rule = ''
            appoint_advance_day = 1
            verify_mode = 1
            valid_period = 2
            use_start_time = None
            use_end_time = None
            refund_mode = 1
            refund_attach_rule = ''
            stock_type = 0
            adult_num = 1
            child_num = 1
            audit_status = 2
            goods_apply_id = None
            spu_status = 1
            user_id = 11000
            deleted = 0
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            modify_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            version = 0

            first_category =  data[17]
            second_category = data[18]
            # 原始的门店id,如果不存在，则跳过
            origin_shop_id = data[10]
            shop_id=shop_id_mapping_dict[origin_shop_id]

            # 商品名称
            spu_name = data[1]
            imgs = data[8]
            cover = data[9]

            poster_img = ''
            goods_guide_id = 0
            sale_start_time = create_time
            d = datetime.datetime.now() + datetime.timedelta(3)
            sale_end_time = d.strftime("%Y-%m-%d %H:%M:%S")
            sort_order = 0

            da_list.append(id)
            da_list.append(third_flag)
            da_list.append(brand_id)
            da_list.append(site_id)
            da_list.append(first_category)
            da_list.append(second_category)
            da_list.append(tenant_id)
            da_list.append(shop_id)
            da_list.append(goods_mode)
            da_list.append(spu_name)
            da_list.append(cover)

            da_list.append(imgs)
            da_list.append(qr_code_img)
            da_list.append(poster_img)
            da_list.append(special_img)
            da_list.append(goods_guide_id)
            da_list.append(goods_blob_id)
            da_list.append(sale_channel)
            da_list.append(sale_visible)
            da_list.append(sale_start_time)
            da_list.append(sale_end_time)
            da_list.append(show_start_count_down)
            da_list.append(show_sale_count_down)
            da_list.append(buy_need_attach)
            da_list.append(buy_attach_rule)
            da_list.append(service_mode)
            da_list.append(sale_mode)
            da_list.append(postage_type)
            da_list.append(postage)
            da_list.append(appoint_need_attach)
            da_list.append(appoint_attach_rule)
            da_list.append(appoint_advance_day)
            da_list.append(verify_mode)
            da_list.append(valid_period)
            da_list.append(use_start_time)
            da_list.append(use_end_time)
            da_list.append(refund_mode)
            da_list.append(refund_attach_rule)
            da_list.append(stock_type)
            da_list.append(adult_num)
            da_list.append(child_num)
            da_list.append(audit_status)
            da_list.append(goods_apply_id)
            da_list.append(spu_status)
            da_list.append(user_id)
            da_list.append(sort_order)
            da_list.append(deleted)
            da_list.append(create_time)
            da_list.append(modify_time)
            da_list.append(version)

            t_data = tuple(da_list)
            args_tuple_list.append(t_data)
        return spu_id_list



    # 将list切割多个
    def split_list(self,data_list, max_size, spilt_data_list):
        if len(data_list) <= max_size:
            spilt_data_list.append(data_list)
            return spilt_data_list
        else:
            spilt_data_list.append(data_list[:max_size])
            return save_item_class.split_list(self,data_list[max_size:], max_size, spilt_data_list)



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
            first_category = 11100003
            second_category = 11100003
            shop_center_id = 11100003
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
            tel = shop_mobile
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


    def insert_data_shop(self,cat_id):
        file_path = 'D:\\project\\python\\沪遇优选商品\\爬取商品门店_'+cat_id+'.csv'
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
        spilt_data_list = save_item_class.split_list(self,data_list, max_size, spilt_data_list)
        # 分批插入spu
        for list1 in spilt_data_list:
            # 保存shop
            shop_sql, shop_args_tuple_list = save_item_class.get_insert_shop_sql(self,list1, self.site_id)
            save_item_class.insert_data(self,shop_sql, shop_args_tuple_list)

    def deal_with_shop_id_mapping(self):
        shop_id_mapping_dict = {}
        sql = "select id,origin_shop_id from shop where deleted =0 and  create_time >'2020-04-25 10:56:58' and site_id =" + str(
            self.site_id)
        conn = pymysql.connect(host=self.host,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.database)
        cursor = conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()
        for data in result:
            shop_id_mapping_dict[data[1]] = data[0]
        cursor.close()
        conn.close()
        return shop_id_mapping_dict


    def get_insert_sku_exts_sql(self,sku_id_list):
        ext_args_tuple_list = []

        for goods_ext_id in sku_id_list:
            ext_data_list = []

            id = IdWorker(1, 2, 0).get_id()
            time.sleep(0.01)
            scope_level=7
            scope_id=goods_ext_id
            exts_type=1
            exts_info='{"extRule":[{"fieldLabel":"返利模式；1-百分比；2-固定金额","fieldName":"benefitMode"},{"fieldLabel":"初级分销商自返利益","fieldName":"juniorSelfBenefit"},{"fieldLabel":"初级分销商团返利益","fieldName":"juniorTeamBenefit"},{"fieldLabel":"中级分销商自返利益","fieldName":"middleSelfBenefit"},{"fieldLabel":"中级分销商团返利益","fieldName":"middleTeamBenefit"},{"fieldLabel":"高级分销商自返利益","fieldName":"seniorSelfBenefit"},{"fieldLabel":"高级分销商团返利益","fieldName":"seniorTeamBenefit"}],"benefitInfo":{"banefitMode":1,"juniorSelfBenefit":0.13,"juniorTeamBenefit":0.25,"middleSelfBenefit":0.22,"middleTeamBenefit":0,"seniorSelfBenefit":0,"seniorTeamBenefit":0}}'
            description='无'
            deleted = 0
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            modify_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            version = 0

            ext_data_list.append(id)
            ext_data_list.append(scope_level)
            ext_data_list.append(scope_id)
            ext_data_list.append(exts_type)
            ext_data_list.append(exts_info)
            ext_data_list.append(description)
            ext_data_list.append(deleted)
            ext_data_list.append(create_time)
            ext_data_list.append(modify_time)
            ext_data_list.append(version)

            t_data = tuple(ext_data_list)
            ext_args_tuple_list.append(t_data)

            goods_ext_sql = 'insert into goods_exts (id,scope_level,scope_id,exts_type,exts_info,description,deleted,create_time,modify_time,version) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        return goods_ext_sql,ext_args_tuple_list


    def save_item_data(self):
        shop_id_mapping_dict=save_item_class.deal_with_shop_id_mapping(self)

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
        # print(data_list)
        # 每批次最大数量
        max_size = 100
        spilt_data_list = save_item_class.split_list(self,data_list, max_size, spilt_data_list)
        spu_id_list = []


        # 分批插入spu
        for list1 in spilt_data_list:
            # 保存spu
            spu_sql, spu_args_tuple_list = save_item_class.get_insert_spu_sql(self,list1, site_id, spu_id_list,shop_id_mapping_dict)
            save_item_class.insert_data(self,spu_sql, spu_args_tuple_list)
        print('spu_id_list长度=', len(spu_id_list), ';spu_id_list=', spu_id_list)
        print('data_list长度=', len(data_list))


        # 保存sku
        sku_sql, sku_args_tuple_list,sku_id_list = save_item_class.get_insert_sku_sql(self,data_list, spu_id_list)
        save_item_class.insert_data(self,sku_sql, sku_args_tuple_list)

        # 保存sku_exts
        goods_ext_sql,ext_args_tuple_list= save_item_class.get_insert_sku_exts_sql(self,sku_id_list)
        save_item_class.insert_data(self, goods_ext_sql,ext_args_tuple_list)


















