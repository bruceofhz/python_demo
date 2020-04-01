#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import threading
import time

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# ip清洗
def checkip(targeturl, ip):
    proxies = {"http": "http://" + ip, "https": "http://" + ip}  # 代理ip
    try:
        response = requests.get(targeturl, False, proxies, header,
                                5).status_code
        if response == 200:
            return True
        else:
            return False
    except:
        return False


# 免费代理 XiciDaili
def findip(type, pagenum, targeturl):  # ip类型,页码,目标url,存放ip的路径
    list = {
        '1': 'http://www.xicidaili.com/nt/',  # xicidaili国内普通代理
        '2': 'http://www.xicidaili.com/nn/',  # xicidaili国内高匿代理
        '3': 'http://www.xicidaili.com/wn/',  # xicidaili国内https代理
        # '4': 'https://www.kuaidaili.com/free/inha/'
    }
    url = list[str(type)] + str(pagenum)  # 配置url
    html = requests.get(url, header).text
    print('代理网站返回html文本:' + html)
    soup = BeautifulSoup(html, 'lxml')
    all = soup.find_all('tr', 'odd')
    for i in all:
        t = i.find_all('td')
        ip = t[1].text + ':' + t[2].text
        print(ip)
        # is_avail = checkip(targeturl, ip)
        # if is_avail == True:
        # write(path=path,text=ip)
        # print(ip)


def getip(targeturl):
    # truncatefile(path) # 爬取前清空文档
    start = datetime.datetime.now()  # 开始时间
    threads = []
    for type in range(3):
        for pagenum in range(5):
            time.sleep(2)
            t = threading.Thread(findip(type + 1, pagenum + 1, targeturl))
            threads.append(t)
    print('开始爬取代理ip')

    for s in threads:  # 开启多线程爬取
        s.start()

    for e in threads:  # 等待所有线程结束
        e.join()
    print('爬取完成')


targeturl = 'https://baidu.com'  # 验证ip有效性的指定url
print(getip(targeturl))
