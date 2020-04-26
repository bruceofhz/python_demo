import os

import requests
from lxml import etree
from retrying import retry

url = 'http://www.quantuwang.co/t/f4543e3a7d545391.html'  # 要爬取的网址

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}  # 头信息

url_list = []  # 建立一个空列表


def url_get():  # 定义网址获取函数，目标是获取可以更改照片序号的网址列表。
    response = requests.get(url, headers=headers)
    html = response.content.decode()
    html1 = etree.HTML(html)  # 获取网页的element
    # 通过Xpath路径找到网页显示的预览照片路径，列表形式赋值给Xpath_html
    xpath_html = html1.xpath('//div/ul[@class="ul960c"]//a/img/@src')

    for x in xpath_html:  # for循环遍历，将网址最后的照片序号改成可格式化输入的格式。
        ix = x.replace('0.jpg', '{}.jpg')
        url_list.append(ix)


url_get()  # 调用上面的函数


@retry(stop_max_attempt_number=3)  # 调用retry模块，将下面的函数装饰--如果报错则重试三次
def pic_get(url2):
    global r  # 声明r为全局变量
    r = requests.get(url2, headers=headers, timeout=5)  # 获取url2信息，并赋值给r


pic = 1  # 定义文件夹的起始序号
for url1 in url_list:  # 遍历照片地址
    os.makedirs('D:\\project\\python\\file\\套图{}'.format(pic))  # 建立文件夹
    for i in range(1, 101):  # 因为没套图的图片数量没有超过100的，所以遍历1-101来获取全部图片的网址
        url2 = url1.format(i)  # 将图片序号循环赋值给网址的{}
        pic_get(url2)  # 调用上面被装饰的函数
        re = r.status_code  # 获取r的头信息，如果遍历的图片地址返回404，则退出循环。
        if re == 404:
            break
        else:
            with open('D:\\project\\python\\file\\套图{}\\pic{}.jpg'.format(pic, i), 'wb') as f:  # 保存照片
                f.write(r.content)
            print('pic{}.jpg'.format(i))  # 打印显示程序运行状态

    pic += 1  # 完成第一个套图的存储，开始生成第个文件夹的序号。
