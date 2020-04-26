from 沪遇优选.最新代码.get_item import get_item_class
from 沪遇优选.最新代码.get_shop import get_shop_class
from 沪遇优选.最新代码.save_item import save_item_class
from 沪遇优选.最新代码.save_shop import save_shop_class

site_id = 11000

host = '192.168.1.52'
user = 'jpss'
passwd = 'Jpss541018!'
database = 'hbsitedb'

goods_category_id_dict = {
    # 美食对应的门店一级和二级类目id
    '18': [1234823381360816128, 1235024460169015296],

    # 亲子
    '19': [1234825032956096512, 1235026545765707776],

    # 丽人
    '29': [1234824686405922816, 1235025522099679232],

    # 生活
    '23': [1234825580560232448, 1235028555554549760]
}

# 门店类目id
shop_category_id_dict = {
    # 美食对应的门店一级和二级类目id
    '18': [1235028620859863040, 1235029134800515072],

    # 亲子
    '19': [1235028711444246528, 1235029696476540928],

    # 丽人
    '29': [1235028682117672960, 1235029542520418304],

    # 生活
    '23': [1235028735859290112, 1235029877611753472]
}

# 门店商圈对应的id
shop_center_id_dict = {
    '161': ['松江新城', 1254237907123396608],

    '164': ['松江老城', 1254238004750016512],

    '188': ['闵行', 1254238040334491648],

    '189': ['金山', 1254238084999634944],

    '190': ['奉贤', 1254238116796653568],

    '191': ['青浦', 1254238147226329088],

    '192': ['嘉定', 1254238178490671104],

    '193': ['其他', 1254238211944439808]
}

shop_data_list = []
item_data_list = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'http://fly.sjfc.cn/',
    'Content-Type': 'application/json; charset=utf-8',
    'Cookie': 'PHPSESSID=idt0ho0rgogebnraqm78t05rmq; snapid=f51043f73cdfa8f1d33459d6f5b5e65e; qsy_6_053user_id=M5QA2FdgeEc0u7Ehm45AAAvE9Mr; SERVERID=68c5f232a35cb17677070b47d390ade3|1586850494|1586850243'
}

if __name__ == '__main__':
    page_size = 30

    # 写入门店csv文件
    file_path1 = 'D:\\project\\python\\沪遇优选商品\\最新\\最新商品门店.csv'
    shop_class = get_shop_class(shop_category_id_dict, shop_center_id_dict, shop_data_list, headers, page_size,
                                file_path1)
    shop_class.write_shop()

    # 写入商品csv文件
    file_path2 = 'D:\\project\\python\\沪遇优选商品\\最新\\最新爬取商品明细.csv'
    item_class = get_item_class(item_data_list, goods_category_id_dict, shop_center_id_dict, headers, page_size,
                                file_path2)
    item_class.write_item()



    # 保存门店数据到数据库
    shop_class_database = save_shop_class(host, user, passwd, database, shop_center_id_dict, site_id,file_path1)
    shop_class_database.save_shop_data()

    # 保存商品数据到数据库
    item_class_database = save_item_class(host, user, passwd, database, site_id,file_path2)
    item_class_database.save_item_data()
