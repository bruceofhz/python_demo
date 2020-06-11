import requests

url = 'https://www.baidu.com/'
robots_txt = 'https://www.jd.com/robots.txt'
agent = 'Mozilla/5.0'

print(agent)

headers = {
    'User-Agent': agent

}
proxies = {
    'https': '223.241.1.145:4216'
}

r = requests.get(url, timeout=50, headers=headers)
r.raise_for_status()
print('apparent_encoding=', r.apparent_encoding)
r.encoding = r.apparent_encoding
print(r.request.headers)
