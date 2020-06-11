import re

# 1.re.match与re.search的区别:re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
# 2.match和 search是匹配一次 ,findall匹配所有,在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(0) : ", matchObj.group(0))
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

print('*****************************')
a = re.match(r'.*ARE.*', line, re.M | re.I)
b = re.search('are.*', line, re.M | re.I)
print(a)
print('b=', b)
print('*****************************')

pattern = re.compile(r'\d+')
print('pattern类型=', type(pattern))
# 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print(m)

m = pattern.match('one12twothree34four', 2, 10)  # 从’e’位置开始查找，没有匹配
print(m)
print('----------------------')

m = pattern.match('one12twothree34four', 3, 10)  # 从‘1’位置开始查找，正好匹配
print(m)
