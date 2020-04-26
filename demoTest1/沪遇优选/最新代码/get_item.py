import csv
import json

import requests



class get_item_class():
    def __init__(self,data_list,goods_category_id_dict,shop_center_id_dict,headers,page_size,file_path):
        self.data_list=data_list
        self.goods_category_id_dict=goods_category_id_dict
        self.shop_center_id_dict = shop_center_id_dict
        self.headers=headers
        self.page_size=page_size
        self.file_path=file_path


    # 获取全部商品id
    def get_items(self,page_size):
        id_list = []

        goods_buiss_data = {}

        for cat_id in self.goods_category_id_dict:
            goods_first_category_id = self.goods_category_id_dict[cat_id][0]
            goods_second_category_id = self.goods_category_id_dict[cat_id][1]

            for cbd_id in self.shop_center_id_dict:

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

                        goods_buiss_data[current_spu_id] = {str(goods_first_category_id), str(goods_second_category_id)}
        return id_list, goods_buiss_data


    # 写入csv文件
    def write_data(self, goods_buiss_data):
        file_path = self.file_path
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            file_name = [
                'id',
                'spu_name',
                'now_price',
                'original_price',
                'show_price',
                'stock',
                'buy_info_status',
                'follow_name',
                'pic_all',
                'pic_main',
                'shop_id',
                'shop_name',
                'shop_address',
                'shop_mobile',
                'shop_hours',
                'lon',
                'lat',
                'goods_first_category_id',
                'goods_second_category_id',
                'new_need_know'
            ]

            f_csv = csv.DictWriter(f, fieldnames=file_name)
            f_csv.writeheader()


            for i in range(len(self.data_list)):
                data = self.data_list[i]
                follow_name = get_item_class.changeField(self,data)

                # 商品名称
                spu_name = data['name']
                format_price = data['format_price']
                # 现价
                now_price = format_price['now_price']
                original_price = format_price['original_price']
                show_price = format_price['show_price']
                kucun = format_price['kucun']

                buy_info_status = data['buy_info_status']
                pic_data = data['pic_all']
                pic_main = pic_data[0]

                pic_all = ''
                for pic in pic_data:
                    pic_all = pic_all + pic + ','

                shop_in = data['shopinfo']

                # 门店信息
                shop_id = ''
                storename = ''
                store_address = ''
                store_mobile = ''
                shop_hours = ''
                lon = ''
                lat = ''
                if len(shop_in):
                    shopinfo = shop_in[0]
                    shop_id = shopinfo['id']
                    storename = shopinfo['storename']
                    store_address = shopinfo['address']
                    store_mobile = shopinfo['mobile']
                    shop_hours = shopinfo['shop_hours']
                    lon = shopinfo['lng']
                    lat = shopinfo['lat']

                # 购买须知
                new_need_know = data['new_need_know']

                spu_id = data['id']
                buiss_data_list = list(goods_buiss_data[spu_id])
                goods_first_category_id = buiss_data_list[0]
                goods_second_category_id = buiss_data_list[1]

                f_csv.writerow({
                    'id': spu_id,
                    'spu_name': spu_name,
                    'now_price': now_price,
                    'original_price': original_price,
                    'show_price': show_price,
                    'stock': kucun,
                    'buy_info_status': buy_info_status,
                    'follow_name': follow_name,
                    'pic_all': pic_all,
                    'pic_main': pic_main,
                    'shop_id': shop_id,
                    'shop_name': storename,
                    'shop_address': store_address,
                    'shop_mobile': store_mobile,
                    'shop_hours': shop_hours,
                    'lon': lon,
                    'lat': lat,
                    'goods_first_category_id': goods_first_category_id,
                    'goods_second_category_id': goods_second_category_id,
                    'new_need_know': new_need_know
                })

    def changeField(self,data):
        follow_name = '-'
        if 'follow_name' in data:
            follow_name = data['follow_name']

        return follow_name

    def append_item_detail(self,fid):
        url = 'http://fly.sjfc.cn/wap/Act/act_info?fid=' + str(fid) + '&share_uid=&coupon_uid='
        response = requests.get(url, headers=self.headers)
        text = response.content.decode()
        json_text = json.loads(text)
        data = json_text['data']
        self.data_list.append(data)


    def write_item(self):
        page_size = self.page_size
        id_list, goods_buiss_data = get_item_class.get_items(self,page_size)


        id_list = list(set(id_list))
        id_list.sort()
        print('商品去重后大小: id_list=', len(id_list),';id_list=',id_list)

        for i in range(len(id_list)):
            get_item_class.append_item_detail(self,id_list[i])

        get_item_class.write_data(self, goods_buiss_data)


