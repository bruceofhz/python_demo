import requests
from bs4 import BeautifulSoup

# 推荐优先使用requests库
url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=20&type=T'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

key_list = {
    '小说',
    '散文',
    # '随笔'
}

# for key in key_list:
#     key_ascii = request.quote(key)
#
#     for num in range(0, 3):
#         page_url = 'https://book.douban.com/tag/' + key_ascii + '?start=' + str(num * 20) + '&type=T'
#         response = requests.get(page_url, headers=headers)
#         data = response.text
#
#         file_path = 'D:\\python保存文件\\' + key + '\\第' + str(num + 1) + '页.html'
#         with open(file_path, 'w', encoding='utf-8') as f:
#             f.write(data)


book_name_list = []

for size in range(0, 10):
    size = size * 20

    page_url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=' + str(size) + '&type=T'
    response = requests.get(page_url, headers=headers)
    data = response.text
    scoup = BeautifulSoup(data, 'html.parser')

    # subject_list > ul > li:nth-child(20) > div.info > h2 > a

    for i in range(1, 21):
        book_name = scoup.select('#subject_list > ul > li:nth-child(' + str(i) + ') > div.info > h2 > a')
        book_name = book_name[0]
        # print(book_name)
        # print('######################')
        name = book_name.get_text().replace('\n', '').replace(' ', '')
        # print(name)
        book_name_list.append(name)

print(book_name_list)
