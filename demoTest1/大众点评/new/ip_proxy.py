import time
from urllib.parse import urljoin

import pymysql
import requests
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()


class MyException(Exception):

    def __init__(self, status, msg):
        self.status = status
        self.msg = msg
        super().__init__()


class XiCi:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": ua.random,
            "Host": "www.xicidaili.com"
        }
        self.conn = pymysql.connect(host="192.168.1.52",

                                    user="jpss",
                                    passwd='Jpss541018!',
                                    db="spreaddb-test")
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_page_html(self, api):
        '''通过get方法请求网页'''
        response = self.session.get(url=api, headers=self.session.headers)
        if response.status_code == 200:
            return response

    def __html_to_etree(self, html):
        '''将html源码转为xml'''
        return etree.HTML(html)

    def get_next_page_url(self, response):
        '''拿到下一页的url'''
        selector = self.__html_to_etree(response.text)
        try:
            next_page_url = selector.xpath("//a[@class='next_page']/@href")[0]
            next_page_url = urljoin(response.url, next_page_url)
            return next_page_url
        except IndexError:
            raise MyException(1000, "爬取完毕")

    def __get_proxies_info(self, response):
        '''获取到爬取的代理信息'''
        selector = self.__html_to_etree(response.text)
        tr_ele_list = selector.xpath("//*[@id='ip_list']//tr")
        for tr in tr_ele_list:
            ip = tr.xpath("td[2]/text()")
            if not ip:
                continue
            ip = ip[0]
            port = tr.xpath("td[3]/text()")[0]
            type = tr.xpath("td[6]/text()")[0]
            yield [ip, port, type]

    def __detect_availability(self, data):
        '''拿到爬取的数据，检测代理是否可以使用'''
        https_api = "https://icanhazip.com/"
        http_api = "http://icanhazip.com/"
        ip = data[0]
        port = data[1]
        type = data[2]
        proxies = {type.lower(): "{}://{}:{}".format(type.lower(), ip, port)}
        try:
            if type.upper() == "HTTPS":
                requests.get(https_api, headers={"User-Agent": ua.random}, proxies=proxies, timeout=3)
            else:
                requests.get(http_api, headers={"User-Agent": ua.random}, proxies=proxies, timeout=3)
            return True
        except Exception:
            return False

    def get_usable_proxies_ip(self, response):
        '''获取到可用的代理ip'''
        res = self.__get_proxies_info(response)
        for data in res:
            if self.__detect_availability(data):
                self.save_to_db(data)

    def save_to_db(self, data):
        '''保存到数据库'''
        sql = 'insert into proxies(ip,port,type) values(%s,%s,%s);'
        print(data)
        self.cursor.execute(sql, data)
        self.conn.commit()

    def run(self, api):
        '''启动入口'''
        page = 1
        while True:
            print("爬取第{}页数据...".format(page))
            response = self.get_page_html(api)
            self.get_usable_proxies_ip(response)
            try:
                api = self.get_next_page_url(response)
            except MyException as e:
                if e.status == 1000:
                    print(e.msg)
                    break
            page += 1
            time.sleep(3)

    # def __del__(self):
    #     self.conn.close()


if __name__ == '__main__':
    api = "https://www.xicidaili.com/nn"
    xici = XiCi()
    xici.run(api)
