import requests
from fake_useragent import UserAgent

agent = UserAgent().random

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Host': 'shop42777801.youzan.com',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    # 'Referer': 'https://shop42777801.m.youzan.com/v2/showcase/homepage?kdt_id=42585633'

}
url = 'http://eclass.lejiaotong.cn/course/explore'


r=requests.session()
r.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
res=r.get(url)


# headers = {
#     'user-agent': agent
# }
# url = 'https://news.qq.com/'

# proxies = {"http": "223.241.1.145:4216"}
# res = requests.get(url, headers=headers, timeout=50, proxies=proxies, allow_redirects=True)
# res.encoding = res.apparent_encoding

print('status_code=', res.status_code)
print(res.text)
