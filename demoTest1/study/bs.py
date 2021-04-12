import re

import requests
from bs4 import BeautifulSoup

req_obj = requests.get('https://www.baidu.com')
soup = BeautifulSoup(req_obj.text, 'lxml')

print(req_obj.text)
print(soup.meta.name)
print(soup.meta.parent.name)

'''标签查找'''
print('title=', soup.title)  # 只是查找出第一个
# print(soup.find('title'))  # 效果和上面一样
# print(soup.find_all('div'))  # 查出所有的div标签

'''获取标签里的属性'''
tag = soup.div
print('---------11111111111------------')
print('attrs***********', soup.div.attrs)
# 查找标签的id属性
print(tag.attrs['id'])


'''标签包的字符串'''
print('-----------222222222----------')
tag = soup.title
print(tag.string)  # 获取标签里的字符串
tag.string.replace_with("哈哈")  # 字符串不能直接编辑，可以替换

'''子节点的操作'''
tag = soup.head
print(tag.title)  # 获取head标签后再获取它包含的子标签

'''contents 和 .children'''
tag = soup.body
print(tag.contents)  # 将标签的子节点以列表返回
print([child for child in tag.children])  # 输出和上面一样

'''descendants'''
tag = soup.body
[print(child_tag) for child_tag in tag.descendants]  # 获取所有子节点和子子节点

'''strings和.stripped_strings'''
tag = soup.body
[print(str) for str in tag.strings]  # 输出所有所有文本内容
[print(str) for str in tag.stripped_strings]  # 输出所有所有文本内容，去除空格或空行

'''.parent和.parents'''
tag = soup.title
print(tag.parent)  # 输出便签的父标签
[print(parent) for parent in tag.parents]  # 输出所有的父标签

'''.next_siblings 和 .previous_siblings
    查出所有的兄弟节点
'''

'''.next_element 和 .previous_element
    下一个兄弟节点
'''

'''find_all的keyword 参数'''
soup.find_all(id='link2')  # 查找所有包含 id 属性的标签
soup.find_all(href=re.compile("elsie"))  # href 参数,Beautiful Soup会搜索每个标签的href属性:
soup.find_all(id=True)  # 找出所有的有id属性的标签
soup.find_all(href=re.compile("elsie"), id='link1')  # 也可以组合查找
soup.find_all(attrs={"属性名": "属性值"})  # 也可以通过字典的方式查找
