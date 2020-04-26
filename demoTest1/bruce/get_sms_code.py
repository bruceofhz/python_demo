import time

import requests
from bs4 import BeautifulSoup

session = requests.session()

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
    file_name = 'D:\\project\\python\\沪遇优选商品\\code.png'
    with open(file_name, 'wb') as f:
        f.write(content)


# 发送验证码
def get_sms_code(img_code):
    url = 'http://fly.sjfc.cn/wap/user/get_sms_code'
    data = {
        "mobile": "17707138916",
        "captcha": img_code
    }

    res = requests.post(url, data=data, headers=headers)
    print(res.text)


cat_id_list = {
    '18': '美食',
    '19': '亲子',
    '9': '酒景',
    '29': '丽人',

}


def get_items():
    url = 'http://fly.sjfc.cn/#/list/b2c_list'
    response = requests.get(url, headers=headers)
    text = response.text
    print(text)

    scoup = BeautifulSoup(text, 'html.parser')
    t = scoup.select(
        '#home > div.hd-search > div.topbar-cate > div.hd > div > div > div:nth-child(2)')
    print(t)

    # data = text.get('data')
    # print(data)
    # list = data.get('list')
    # print('###############')
    #
    # list = list[0]
    #
    # file_path = 'D:\\project\\python\\沪遇优选商品\\美食.csv'
    # for i in range(len(list)):
    #
    #     print(list[i])
    #     with open(file_path, 'w', newline='', encoding='utf-8') as f:
    #         file_name = [
    #             'name',
    #             'pic',
    #             'format_price'
    #         ]
    #         f_csv = csv.DictWriter(f, fieldnames=file_name)
    #         f_csv.writeheader()
    #         for i in range(len(list)):
    #             f_csv.writerow({
    #                 'name': list[i].get('name'),
    #                 'pic': list[i].get('pic'),
    #                 'format_price': list[i].get('format_price')
    #             })
    #
    # print('####################')


def login():
    # 下载图片验证码
    code_img()

    img_code = input('图片验证码:')

    # 根据手机号和图片验证码，发送短信验证码
    get_sms_code(img_code)

    print('#############')
    sms_code = input('输入短信验证码:')

    # 登录
    url = 'http://fly.sjfc.cn/wap/user/login'
    data = {
        "mobile": "17707138916",
        "sms_code": sms_code
    }

    print(sms_code)

    res = requests.post(url, data=data, headers=headers)
    print(res.text)


if __name__ == '__main__':
    login()
    get_items()
