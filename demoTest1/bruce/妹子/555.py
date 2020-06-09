import requests

headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    'Connection': 'Keep-Alive',
    'Referer': "http://www.mzitu.com/"
}

urls = [
    # 性感妹子
    "https://www.mzitu.com/xinggan/",
    # 日本妹子
    "https://www.mzitu.com/japan/",
    # 台湾妹子
    "https://www.mzitu.com/taiwan/",
    # 清纯妹子
    "https://www.mzitu.com/mm/",
]

if __name__ == '__main__':
    url = urls[0]
    response = requests.get(url=url, headers=headers)
    print(response.text)
