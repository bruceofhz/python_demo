import requests

url = 'https://www.baidu.com/'
robots_txt='https://www.jd.com/robots.txt'

proxies = {
    'https': '223.241.1.145:4216'
}

try:
    page = requests.get(url, timeout=20, proxies=proxies)
    page.raise_for_status()
    print('apparent_encoding=', page.apparent_encoding)
    page.encoding = page.apparent_encoding
    print(page.text)
except:
    print("异常")
