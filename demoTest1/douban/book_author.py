import csv

import requests
from bs4 import BeautifulSoup

# 推荐优先使用requests库
url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=20&type=T'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

book_list = []

book_name_list = []
author_list = []
time_list = []
score_list = []


def get_book_list():
    for size in range(0, 20):
        size = size * 20

        page_url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=' + str(size) + '&type=T'
        response = requests.get(page_url, headers=headers)
        data = response.text
        scoup = BeautifulSoup(data, 'html.parser')

        for i in range(1, 9):
            # 书名
            book_name = scoup.select('#subject_list > ul > li:nth-child(' + str(i) + ') > div.info > h2 > a')
            book_name = book_name[0]
            book_name = book_name.get_text().replace('\n', '').replace(' ', '')
            book_name_list.append(book_name)

            author_time = scoup.select('#subject_list > ul > li:nth-child(' + str(i) + ') > div.info > div.pub')
            author_time = author_time[0]
            text = author_time.get_text().replace('\n', '').replace(' ', '')
            data = text.split('/')
            author_list.append(data[0])
            time_list.append(data[-1])

            # 评分
            score = scoup.select(
                '#subject_list > ul > li:nth-child(' + str(i) + ') > div.info > div.star.clearfix > span.rating_nums')
            score = score[0]
            score = score.get_text().replace('\n', '').replace(' ', '')
            score_list.append(score)

            # print(data[0])
            # print('size=' + str(size) + ';i=' + str(i))
            # print(data)
            # if (None is data[0]):
            #     author_list.append('null')
            #     time_list.append('null')
            # else:
            #     author_list.append(data[0])
            #     time_list.append(data[-1])
            # print('\t')

    for i in range(len(author_list)):
        book_list.append(
            {
                '作者': author_list[i],
                '时间': time_list[i],
                '评分': score_list[i],
                '书名': book_name_list[i]
            }
        )
    return book_list


# print('author_list=' + str(author_list))
# print('time_list=' + str(time_list))
# print('score_list=' + str(score_list))

if __name__ == '__main__':
    book_list = get_book_list()
    print(book_list)

    file_path = 'D:\\python保存文件\\book.csv'
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        file_names = [
            '作者',
            '时间',
            '评分',
            '书名',
            '3333'
        ]
        f_csv = csv.DictWriter(f, fieldnames=file_names)
        f_csv.writeheader()
        for i in range(len(author_list)):
            f_csv.writerow(
                {
                    '作者': author_list[i],
                    '时间': time_list[i],
                    '评分': score_list[i],
                    '书名': book_name_list[i]
                }
            )
