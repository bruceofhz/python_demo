import csv
import json
import time

import requests

url = 'http://fly.sjfc.cn/#/comment/index'
# url = 'https://accounts.douban.com/passport/login?source=book'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'http://fly.sjfc.cn/'
}


# 获取图片验证码,并写入本地
def code_img():
    timestamp = (int(round(time.time() * 1000)))
    code_url = 'http://fly.sjfc.cn/wap/user/get_captcha?t=' + str(timestamp)
    print(code_url)

    response = requests.get(code_url, headers=headers)
    content = response.content
    file_name = 'D:\\python保存文件\\验证码\\code.png'
    with open(file_name, 'wb') as f:
        f.write(content)


def get_sms_code():
    url = 'http://fly.sjfc.cn/wap/user/get_sms_code'
    data = {
        "mobile": "17707138916",
        "captcha": code_img()
    }
    res = requests.post(url, data=data, headers=headers)


cat_id_list = {
    '18': '美食',
    '19': '亲子',
    '9': '酒景',
    '29': '丽人',

}


def get_items():
    for page in range(1, 7):
        url = 'http://fly.sjfc.cn/wap/Act/b2c_ajax?cat_id=18&page=' + str(page) + '&type=cat'
        response = requests.get(url, headers=headers)
        text = response.text

        json_text = json.loads(text)

        print('json解析后' + json_text)

        data = text.get('data')
        print(data)
        list = data.get('list')
        print('###############')

        if (None is list):
            break
        # print('list的长度:' + str(len(list)))
        list = list[0]

        file_path = 'D:\\project\\python\\沪遇优选商品\\美食.csv'
        for i in range(len(list)):

            print(list[i])
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                file_name = [
                    'name',
                    'pic',
                    'format_price'
                ]
                f_csv = csv.DictWriter(f, fieldnames=file_name)
                f_csv.writeheader()
                for i in range(len(list)):
                    f_csv.writerow({
                        'name': list[i].get('name'),
                        'pic': list[i].get('pic'),
                        'format_price': list[i].get('format_price')
                    })

        print('####################')

        # scoup = BeautifulSoup(text, 'html.parser')
        # t = scoup.select(
        #     '#home > div.van-pull-refresh > div > div.bd-wrap > div:nth-child(12) > div.my-vant-list > div > div.list.small > div:nth-child(1) > a > div.bd > div.bd_tit')
        #
        # print(t)


def login():
    url = 'http://fly.sjfc.cn/wap/user/login'
    data = {
        "mobile": "17707138916",
        "sms_code": input('输入短信验证码：')
    }

    # 将字典转换为json数据
    j = json.dumps(data)
    print(j)
    res = requests.post(url, data=data, headers=headers)

    print(res.text)


if __name__ == '__main__':
    # login()
    get_items()
