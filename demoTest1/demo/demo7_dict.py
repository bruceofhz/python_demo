dict1 = {
    'abc': 123,
    12: 34
}

print(dict1['abc'])

# 如果用字典里没有的键访问数据，会输出错误
print(dict1[12])
# print(dict1['2'])

dict2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# 更新
dict2['Age'] = 8
print(dict2)
# 新增
dict2['哈哈'] = '呵呵'
print(dict2)
