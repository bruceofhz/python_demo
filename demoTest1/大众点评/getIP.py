import requests
from lxml import etree

# headers = {'User-Agent': UserAgent().random}
# url = 'http://www.dianping.com/hangzhou/ch70/g34313'
url = 'https://blog.csdn.net/orangefly0214/article/details/81387077'


class GetIp:
    def __init__(self, headers):
        self.headers = headers

    def getListProxies(self):
        url = 'https://www.kuaidaili.com/free/'
        page = requests.session().get("http://www.xicidaili.com/nn", headers=self.headers)
        text = page.text
        # print(text)

        html = etree.HTML(text)
        ip_list = list();
        ips = html.xpath('//tr[@class="odd"]/td[2]/text()')
        ports = html.xpath('//tr[@class="odd"]/td[3]/text()')
        for ip in ips:
            i = ips.index(ip)
            port = ports[i]
            # print('ip=', ip, 'port=', port)
            t = ip + ':' + port
            ip_list.append(t)
        return ip_list

    # def login():
    #     s = requests.get(url, headers)
    #     print(s.cookies)
    #
    # start = 0
    # while (True):
    #     start = start + 1
    #     ip = getListProxies()[start]
    #     print(ip)
    #
    #     response = requests.get(url, ip)
    #     if (response.status_code != 200):
    #         print('访问失败ip=', ip)
    #         continue
    #     else:
    #         break
    #     print(response.text)
