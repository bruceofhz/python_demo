import csv

from 站点.common_method import common_method_get


class get_item_class():
    def __init__(self, data_list, goods_category_id_dict, shop_category_id_dict, shop_center_id_dict, headers,
                 page_size, shop_file_path, item_file_path):
        self.data_list = data_list
        self.goods_category_id_dict = goods_category_id_dict
        self.shop_category_id_dict = shop_category_id_dict
        self.shop_center_id_dict = shop_center_id_dict
        self.headers = headers
        self.page_size = page_size
        self.shop_file_path = shop_file_path
        self.item_file_path = item_file_path

    # 获取全部商品id
    def get_items(self, page_size):
        id_list = []
        goods_buiss_data = {}

        for page in range(1, page_size):
            for cat_id in self.goods_category_id_dict:
                goods_first_category_id = self.goods_category_id_dict[cat_id][0]
                goods_second_category_id = self.goods_category_id_dict[cat_id][1]

                shop_first_category_id = self.shop_category_id_dict[cat_id][0]
                shop_second_category_id = self.shop_category_id_dict[cat_id][1]
                for cbd_id in self.shop_center_id_dict:
                    shop_center_id = self.shop_center_id_dict[cbd_id][1]
                    print('page=', page, ',cat_id=', cat_id, ',cbd_id=', cbd_id)
                    item_url = 'http://2382.bd.aiyichuan.com/wap/Act/b2c_ajax?type=cat&cat_id=' + cat_id + '&order=back&cbd_id=' + cbd_id + '&b2c_p_cat_id=&page=' + str(
                        page)
                    print('url=', item_url)
                    data = common_method_get(item_url, self.headers).do_get()
                    item_list = data['list']
                    print('item_list=', item_list)
                    # 商品
                    if (None is item_list):
                        continue
                    for i in range(len(item_list)):
                        a = item_list[i]
                        current_spu_id = a['id']
                        id_list.append(current_spu_id)
                        base_dict_data = {}
                        base_dict_data['goods_first_category_id'] = goods_first_category_id
                        base_dict_data['goods_second_category_id'] = goods_second_category_id

                        base_dict_data['shop_first_category_id'] = shop_first_category_id
                        base_dict_data['shop_second_category_id'] = shop_second_category_id
                        base_dict_data['shop_center_id'] = shop_center_id
                        goods_buiss_data[current_spu_id] = base_dict_data
        return id_list, goods_buiss_data



    def distinct_shop_id(self):
        new_data_list = []

        shop_id_list = []
        shop_id_dict = {}
        for data in self.data_list:
            if 'shopinfo' in data:
                shopinfo = data['shopinfo']
                # 门店信息
                if len(shopinfo) == 0:
                    continue
                else:
                    shopinfo_t = shopinfo[0]
                    shop_id = shopinfo_t['id']

                shop_id_list.append(shop_id)
                shop_id_dict[shop_id] = data
            else:
                continue

        shop_id_set = set(shop_id_list)
        new_shop_id_list = list(shop_id_set)
        new_shop_id_list.sort()

        print('new_shop_id_list长度=', len(new_shop_id_list), ';new_shop_id_list=', new_shop_id_list)
        for i in new_shop_id_list:
            new_data_list.append(shop_id_dict[i])

        return new_data_list

    # 写入csv文件
    def write_data(self, goods_buiss_data, data_list_distinct):
        shop_file_path = self.shop_file_path
        item_file_path = self.item_file_path
        with open(item_file_path, 'w', newline='', encoding='utf-8') as f:
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
                if 'name' in data:
                    # 商品名称
                    spu_name = data['name']
                    format_price = data['format_price']
                    follow_name, kucun = get_item_class.changeField(self, data, format_price)
                    # 现价
                    now_price = format_price['now_price']
                    original_price = format_price['original_price']
                    show_price = format_price['show_price']
                    buy_info_status = data['buy_info_status']
                    pic_data = data['pic_all']
                    pic_main = pic_data[0]

                    pic_all = ''
                    for pic in pic_data:
                        pic_all = pic_all + pic + ','
                    shop_in = data['shopinfo']

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

                        # 购买须知
                        new_need_know = data['new_need_know']
                        spu_id = data['id']
                        buiss_data_list = goods_buiss_data[spu_id]
                        goods_first_category_id = buiss_data_list['goods_first_category_id']
                        goods_second_category_id = buiss_data_list['goods_second_category_id']
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
                else:
                    continue

        with open(shop_file_path, 'w', newline='', encoding='utf-8') as f:
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

                buiss_data_dict = goods_buiss_data[spu_id]
                shop_first_category_id = buiss_data_dict['shop_first_category_id']
                shop_second_category_id = buiss_data_dict['shop_second_category_id']
                shop_center_id = buiss_data_dict['shop_center_id']
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

    def changeField(self, data, format_price):
        follow_name = '-'
        if 'follow_name' in data:
            follow_name = data['follow_name']

        kucun = '-'
        if 'kucun' in data:
            kucun = format_price['kucun']
        return follow_name, kucun

    def append_item_detail(self, fid):
        url = 'http://fly.sjfc.cn/wap/Act/act_info?fid=' + str(fid) + '&share_uid=&coupon_uid='
        data = common_method_get(url, self.headers).do_get()
        self.data_list.append(data)

    def write_item(self):
        page_size = self.page_size
        id_list, goods_buiss_data = get_item_class.get_items(self, page_size)

        id_list = list(set(id_list))
        id_list.sort()
        print('商品去重后大小: id_list=', len(id_list), ';id_list=', id_list)

        for i in range(len(id_list)):
            get_item_class.append_item_detail(self, id_list[i])

        data_list_distinct = get_item_class.distinct_shop_id(self)
        get_item_class.write_data(self, goods_buiss_data, data_list_distinct)
