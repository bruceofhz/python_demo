import random
import time

import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'content-type': 'charset=utf8'
}
url = 'http://m.hxnews.com/news/gn/shxw/202003/24/1876211.shtml'
# url = 'https://movie.douban.com/'

proxy_ip = {
    'https': 'https://59.37.18.243:3128'

}

# 获取代理ip
ips = open('proxies.text', 'r').read().split('\n')


def get_random_ip():
    ip = random.choice(ips)
    pxs = {ip.split(':')[0]: ip}
    return pxs


def getHtml(url, header):
    try:
        time.sleep(random.random() * 6)
        response = requests.get(url, header)

        response.encoding = 'utf8'
        return response.text
    except Exception as e:
        print('异常', e)

        return '异常'


print(getHtml(url, header))
print(get_random_ip())
