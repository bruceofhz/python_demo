import csv
import json

import requests
import logging





class get_shop_class(object):
    def __init__(self,shop_category_id_dict, shop_center_id_dict, data_list, headers,page_size,file_path):
        self.shop_category_id_dict = shop_category_id_dict
        self.shop_center_id_dict = shop_center_id_dict
        self.data_list = data_list
        self.headers = headers
        self.page_size = page_size
        self.file_path = file_path

    def distinct_shop_id(self):
        new_data_list = []

        shop_id_list = []
        shop_id_dict = {}
        for data in self.data_list:
            shop_in = data['shopinfo']
            # 门店信息
            if len(shop_in) == 0:
                continue
            else:
                shopinfo = shop_in[0]
                shop_id = shopinfo['id']

            shop_id_list.append(shop_id)
            shop_id_dict[shop_id] = data

        shop_id_set=set(shop_id_list)
        new_shop_id_list = list(shop_id_set)
        new_shop_id_list.sort()

        print('new_shop_id_list长度=', len(new_shop_id_list),';new_shop_id_list=',new_shop_id_list)
        for i in new_shop_id_list:
            new_data_list.append(shop_id_dict[i])

        return new_data_list



    # 获取全部商品id
    def get_shops(self,page_size):
        id_list = []

        # 商品id对应的门店类目id和门店商圈id信息
        shop_buiss_data = {}

        for cat_id in self.shop_category_id_dict:
            shop_first_category_id = self.shop_category_id_dict[cat_id][0]
            shop_second_category_id = self.shop_category_id_dict[cat_id][1]

            for cbd_id in self.shop_center_id_dict:
                shop_center_id = self.shop_center_id_dict[cbd_id][1]

                for size in range(page_size):
                    url = 'http://fly.sjfc.cn/wap/Act/b2c_ajax?type=cat&cat_id=' + cat_id + '&page=' + str(
                        size) + '&cbd_id=' + cbd_id
                    response = requests.get(url, headers=self.headers)
                    text = response.content.decode()

                    json_text = json.loads(text)
                    data = json_text['data']
                    list = data['list']

                    # 商品
                    if (None is list):
                        break
                    for i in range(len(list)):
                        a = list[i]
                        current_spu_id = a['id']
                        id_list.append(current_spu_id)

                        print('current_spu_id=', current_spu_id, ';shop_first_category_id=', shop_first_category_id,
                              ';shop_second_category_id=', shop_second_category_id, ';shop_center_id=', shop_center_id)

                        shop_buiss_data[current_spu_id] = {str(shop_first_category_id), str(shop_second_category_id),
                                                           str(shop_center_id)}

        return id_list, shop_buiss_data


    # 写入csv文件
    def write_data_shop(self, data_list_distinct,shop_buiss_data):
        file_path = self.file_path
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            file_name = [
                'shop_id',
                'shop_name',
                'shop_address',
                'shop_mobile',
                'shop_hours',
                'lon',
                'lat',
                'shop_first_category_id',
                'shop_second_category_id',
                'shop_center_id'
            ]

            f_csv = csv.DictWriter(f, fieldnames=file_name)
            f_csv.writeheader()

            for i in range(len(data_list_distinct)):
                data = data_list_distinct[i]
                spu_id = data['id']
                shop_in = data['shopinfo']

                # 门店信息
                if len(shop_in) == 0:
                    continue
                else:
                    shopinfo = shop_in[0]
                    shop_id = shopinfo['id']
                    storename = shopinfo['storename']
                    store_address = shopinfo['address']
                    store_mobile = shopinfo['mobile']
                    shop_hours = shopinfo['shop_hours']
                    lon = shopinfo['lng']
                    lat = shopinfo['lat']

                buiss_data_list = list(shop_buiss_data[spu_id])
                shop_first_category_id = buiss_data_list[0]
                shop_second_category_id = buiss_data_list[1]
                shop_center_id = buiss_data_list[2]
                f_csv.writerow({
                    'shop_id': shop_id,
                    'shop_name': storename,
                    'shop_address': store_address,
                    'shop_mobile': store_mobile,
                    'shop_hours': shop_hours,
                    'lon': lon,
                    'lat': lat,
                    'shop_first_category_id': shop_first_category_id,
                    'shop_second_category_id': shop_second_category_id,
                    'shop_center_id': shop_center_id
                })


    def append_item_detail(self,fid):
        url = 'http://fly.sjfc.cn/wap/Act/act_info?fid=' + str(fid) + '&share_uid=&coupon_uid='
        response = requests.get(url, headers=self.headers)
        text = response.content.decode()
        json_text = json.loads(text)
        data = json_text['data']
        self.data_list.append(data)


    def deal_with_data_list(self):
        id_list = []

        for data in self.data_list:
            shop_in = data['shopinfo']
            # 门店信息
            if len(shop_in) == 0:
                continue
            else:
                shopinfo = shop_in[0]
                shop_id = shopinfo['id']
            id_list.append(shop_id)
        print(id_list)

        # 去重
        print('id_list长度去重前=' + str(len(id_list)))
        id_list = list(set(id_list))
        id_list.sort()
        print(id_list)
        print('id_list长度去重后=' + str(len(id_list)))
        return self.data_list


    def write_shop(self):
        page_size = self.page_size
        id_list, shop_buiss_data = get_shop_class.get_shops(self,page_size)

        # print('去重前大小: id_list=', len(id_list), 'shop_buiss_data=', len(shop_buiss_data))

        id_list = list(set(id_list))
        id_list.sort()

        for i in range(len(id_list)):
            # 获取商品明细数据
            get_shop_class.append_item_detail(self,id_list[i])

        # print('商品去重后大小data_list=', len(self.data_list), ';shop_buiss_data=', len(shop_buiss_data))


        # 门店id去重 data_list_distinct=
        data_list_distinct=get_shop_class.distinct_shop_id(self)

        get_shop_class.write_data_shop(self,data_list_distinct, shop_buiss_data)



