import re

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def getListProxies():
    ip_list = []
    session = requests.session()
    headers = {'User-Agent': UserAgent().random}
    page = session.get("http://www.xicidaili.com/nn", headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
    for trtag in taglist:
        tdlist = trtag.find_all('td')
        proxy = {'http': 'http://' + tdlist[1].string + ':' + tdlist[2].string}
        ip_list.append(proxy)
    return ip_list


ip_list = getListProxies()

proxy = ip_list[0]
print(proxy)
while 1:
    headers = {'User-Agent': UserAgent().random,
               'Referer': 'https://m.dianping.com/shenzhen/ch10/r1949'}
    url = 'http://www.dianping.com/hangzhou/ch70/g34313p2'

    s = requests.session()
    respon = s.get(url, headers=headers, proxies=proxy)
    print('respon=', respon, 'text=', respon.text)
