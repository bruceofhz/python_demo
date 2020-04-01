import os
import re

import requests
import xlwt


def get_movie_info(images_path):
    # 初始化并创建一个工作簿
    book = xlwt.Workbook()
    # 创建一个名为movie的表单
    sheet = book.add_sheet('movie', True)  # 加入cell_overwrite_ok在同一单元格重复写入数据
    # 设置表单头部
    headings = [u'排名', u'电影名称', u'导演', u'国家', u'年份', u'评分']
    # 将headings信息写入excel
    k = 0
    for j in headings:
        sheet.write(0, k, j)
        k = k + 1
    # 头部信息
    headers = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    count = 1
    proxies = {
        "http": "http://221.4.150.7",
    }

    for i in range(0, 250, 25):
        url = ' https://movie.douban.com/top250?start=' + str(i) + '&filter='
        r = requests.request('get', url, headers, proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text = r.text  # 得到整个页面信息
        movie_info = re.findall(r'div class="pic">([\d\D]*?)<span property="v:best"', text)  # 筛选出包含电影的信息

        for i in movie_info:
            # 下面依次是获得排名，电影名称，导演，年份和国家，评分，图片的链接
            rank = re.findall(r'<em class="">([\d]*)</em>', i)
            name = re.findall(r'<img width="100" alt="([\d\D]*?)" src=', i)
            director = re.findall(r'导演:([\d\D]*?)&nbsp;.*?', i)
            year_and_country = re.findall(r'<br>\n([\d\D]*?)&nbsp;/&nbsp;([\d\D]*?)&nbsp;/&nbsp;', i)
            score = re.findall(r'<span class="rating_num" property="v:average">([\d.\d]*)', i)
            image_url = re.findall(r'src="([\d\D]*?)" class="">', i)
            # 将信息写入excel
            if ('...' in director[0]):
                director[0] = director[0].split('...')[0]
            # 写入excel文件,三个参数分别是　行号，列号，值
            sheet.write(count, 0, rank)
            sheet.write(count, 1, name)
            sheet.write(count, 2, director)
            sheet.write(count, 3, year_and_country[0][1].strip())
            sheet.write(count, 4, year_and_country[0][0].strip())
            sheet.write(count, 5, score)
            count = count + 1
            # 将图片写入文件夹
            path = image_url[0].split("/")[-1]  # 将图片链接的后面几个数字命名为图片名字
            if not os.path.exists(images_path):  # 目录不存在创建目录
                os.mkdir(images_path)
            if not os.path.exists(images_path + '/' + path):  # 文件不存在则下载
                r = requests.get(image_url[0])
                f = open(images_path + '/' + path, "wb")
                f.write(r.content)
                f.close()
                print("文件下载成功")
            else:
                print("文件已经存在")
    # 保存excel文件
    book.save('电影信息.xls')


if __name__ == '__main__':
    get_movie_info('./images')
    f = 0
    for i in os.listdir('./images'):  # 取得图片数量，看是否是250张
        f = f + 1

print(f)
