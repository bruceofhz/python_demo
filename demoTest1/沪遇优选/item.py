import csv
import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'http://fly.sjfc.cn/',
    'Content-Type': 'application/json; charset=utf-8',
    'Cookie': 'PHPSESSID=idt0ho0rgogebnraqm78t05rmq; snapid=f51043f73cdfa8f1d33459d6f5b5e65e; qsy_6_053user_id=M5QA2FdgeEc0u7Ehm45AAAvE9Mr; SERVERID=68c5f232a35cb17677070b47d390ade3|1586850494|1586850243'
}

dict_data = {
    '9': '酒景',
    '18': '美食'

}


# 获取普通商品
def get_items(cat_id):
    data_list = []
    for size in range(14):
        url = 'http://fly.sjfc.cn/wap/Act/b2c_ajax?cat_id=' + str(cat_id) + '&page=' + str(size) + '&type=cat'

        response = requests.get(url, headers=headers)
        text = response.content.decode()

        json_text = json.loads(text)
        data = json_text['data']
        list = data['list']

        # 商品
        if (None is list):
            break
        for i in range(len(list)):
            data_list.append(list[i])

    return data_list


# 写入csv文件
def write_data(cat_id, data_list):
    name = dict_data[cat_id]
    file_path = 'D:\\project\\python\\沪遇优选商品\\' + name + '.csv'
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        file_name = [
            'name',
            'pic',
            'now_price',
            'form_discount',
            'level_price',
            'show_price',
            'cha_price',
            'original_price',
            'y_show_price',
            'views',
            'tag',
            'type',
            'kucun',
            'is_xiajia',
            'base_sale',
            'jifen',
            'is_cart'
        ]
        f_csv = csv.DictWriter(f, fieldnames=file_name)
        f_csv.writeheader()
        for i in range(len(data_list)):
            data = data_list[i]
            format_price = data['format_price']

            form_discount = '-'
            if 'form_discount' in format_price:
                form_discount = format_price['form_discount']

            kucun = '-'
            if 'kucun' in format_price:
                kucun = format_price['kucun']

            f_csv.writerow({
                'name': data['name'],
                'pic': data['pic'],
                'now_price': format_price['now_price'],
                'form_discount': form_discount,
                'level_price': format_price['level_price'],
                'show_price': format_price['show_price'],
                'cha_price': format_price['cha_price'],
                'original_price': format_price['original_price'],
                'y_show_price': format_price['y_show_price'],
                'views': format_price['views'],
                'tag': format_price['tag'],
                'type': format_price['type'],
                'kucun': kucun,
                'is_xiajia': format_price['is_xiajia'],
                'base_sale': format_price['base_sale'],
                'jifen': format_price['jifen'],
                'is_cart': format_price['is_cart']
            })


if __name__ == '__main__':

    for key in dict_data:
        cat_id = key
        name = dict_data[cat_id]

        data_list = get_items(cat_id)
        print('商品数量' + str(len(data_list)))
        write_data(cat_id, data_list)
