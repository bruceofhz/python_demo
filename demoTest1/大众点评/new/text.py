import urllib

from fake_useragent import UserAgent

agent = UserAgent().random
print(agent)

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'www.dianping.com',
    'user-agent': agent,
    'Referer': 'http://www.dianping.com/hangzhou/ch70/g34313p3',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': '_lxsdk_cuid=171672e084dc8-00039f21aeaa99-3f6b490f-1fa400-171672e084dc8; _lxsdk=171672e084dc8-00039f21aeaa99-3f6b490f-1fa400-171672e084dc8; _hc.v=9a8243e6-92cc-5b2a-c55d-e2eacbe6403b.1586574003; s_ViewType=10; aburl=1; cy=1; cye=shanghai; ctu=1b6de1877873d8e4cc79d2aa5b9073f93781a4810499a1d19bcffe929a7f5ad0; m_flash2=1; cityid=3; default_ab=index%3AA%3A3; switchcityflashtoast=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1591684107,1591860004; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1591684107,1591686007,1591860004; thirdtoken=ad7c3c87-7b15-4a8e-a1df-d0638bec884d; dper=9fcb15eec3c6fc8ba00c2e3459a5b0c6355dd7c4c2917af311e11a0fd89f42f8a7d0490c7fa8b9b043529f1f83b1743d5e6c4a2173fbfb74ced277523242a617b6d8a5f18d5890678c617feb65e7960b97a818142298c10f69aa5b9ee7d225a5; ll=7fd06e815b796be3df069dec7836c3df; ua=enter; ctu=32f4055f03a815bda5469a48e28944b20d62350cc44a946d9faea569f907641bc8d03fffa8b614a93eaff19dc03fef7c; dplet=8c5745fb1b755a5eb544031041c3e04d; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1591864988; _lxsdk_s=172a28bee20-d7f-e68-4ff%7Cuser-id%7C6; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1591864999'
}
url = 'http://www.dianping.com/hangzhou/ch70/g34313p3'

# header = {
#     'user-agent': agent
# }
# url = 'https://news.qq.com/'

proxy_handler = urllib.request.ProxyHandler({"http": "223.241.1.145:4216"})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)
req = urllib.request.Request(url=url, headers=header)
res = urllib.request.urlopen(req)
print(res.read())
print(res.read().decode('utf-8'))
