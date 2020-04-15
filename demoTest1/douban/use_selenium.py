import re

from bs4 import BeautifulSoup
from selenium import webdriver

# url = 'https://www.bilibili.com/'
url = 'http://fly.sjfc.cn/#/my/index'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'http://fly.sjfc.cn/'
}


def ss():
    driver = webdriver.Chrome()
    driver.get(url)

    page = driver.page_source
    scoup = BeautifulSoup(page, 'html.parser')
    code = scoup.select(
        'body > div > main > div.page-login.van-popup.van-popup--center > div > div.vcode.inpubox > img')
    print(code)
    code = code[0]
    return code


def get_src_url(code):
    pattern = 'src="(.*)"/> '
    obj = re.compile(pattern)
    res = obj.findall(code)
    print(res[0])


if __name__ == '__main__':
    code = ss()
    print(type(code))
    print('##########')
    print(str(code))
    get_src_url(code)
