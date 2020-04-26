import urllib.request

import requests

# 推荐优先使用requests库
url = 'https://www.bilibili.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def use_urllib():
    # response = urllib.request.urlopen(url)
    # data = response.read().decode()

    req = urllib.request.Request(url, headers=headers)
    print(req)


def use_requests():
    response = requests.get(url, headers)

    data = response.content.decode()
    print(data)

    # 写入到本地文件
    file_path = 'D:\\python保存文件\\bilibili.html'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)


if __name__ == '__main__':
    # use_urllib()
    use_requests()
