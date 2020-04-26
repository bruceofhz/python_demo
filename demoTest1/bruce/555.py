from lxml import etree

text = '''
<p><strong><span style="color: #ff0000;">未使用可随时退款，不收取手续费，请放心购买</span></strong></p>
<p> </p>
<p><strong><span style="color: #ff0000;">➤ 商品介绍：</span></strong><span style="color: #000000;">「 隆程港式餐厅」豪华套餐</span><span style="background-color: #ffffff;"><span style="color: #000000;">，</span>见商品详情</span></p>
<p> </p>
<p><strong><span style="color: #ff0000;">➤使用须知</span>：</strong>即日起至2020年5月31，用餐时间10:00-21:00；周末及法定节假日通用，<strong>周末及节假日需提前1天预约</strong></p>
<p> </p>
<p><span style="color: #ff0000;"><strong>➤使用规则：</strong></span></p>
<p>1.每人不限购，每人每次限用1张券；仅限堂食</p>
<p>2.本活动不与店内其他优惠同享；到店需出示订单二维码核销使用</p>
'''



print(text)
print('----------------------------')
html = etree.HTML(text,etree.HTMLParser())  # 初始化生成一个XPath解析对象
result=html.xpath('//strong/span/text()')
print(result)
