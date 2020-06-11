import os

import requests

url = 'http://img1.xcarimg.com/b11/s4316/20130406095854185235.jpg-908x681.jpg'
root = 'F://爬虫存储路径//'

path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print('文件已存在')

except:
    print('失败')
