from lxml import etree

if __name__ == '__main__':
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a> 
         </ul>
    </div>
    '''

    # 初始化一个xpath解析对象
    html = etree.parse(text)
    result = etree.tostring(html, encoding='utf-8')
    print(type(html))
    print(type(result))
    print(result.decode('utf-8'))
