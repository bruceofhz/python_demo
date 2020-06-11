import requests

try:
    url = 'https://www.baidu.com'
    kv = {'wd': 'python'}
    r = requests.get(url, params=kv)
    print(r.status_code)
    print(r.request.url)
    print(r.text)
except:
    print("异常")
