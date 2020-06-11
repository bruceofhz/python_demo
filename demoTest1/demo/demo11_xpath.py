from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="www.baidu.com">baidu</a>
        <li class="item-1"><a href="https://blog.csdn.net/qq_25343557">myblog</a>
        <li class="item-2"><a href="https://www.csdn.net/">csdn</a>
        <li class="item-3"><a href="https://hao.360.cn/?a1004">hao123</a>
'''

# 补全html标签
html = etree.HTML(text)
result = etree.tostring(html)
print('result类型=', type(result))
print(result.decode('utf-8'))
print('--------------------------------')

a = html.xpath('//a/text()')
print(a)
print(html.xpath('//a/@href'))
