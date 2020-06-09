from 沪遇优选.最新代码.save_item import save_item_class
from 沪遇优选.最新代码.save_shop import save_shop_class
from 站点 import config
from 站点.common_method import common_method_get
from 站点.get_item import get_item_class

headers = config.headers

host = config.host
user = config.user
passwd = config.passwd
database = config.database

goods_category_id_dict = config.goods_category_id_dict

# 门店类目id
shop_category_id_dict = config.shop_category_id_dict

# 门店商圈对应的id
shop_center_id_dict = config.shop_center_id_dict


def get_item_list(page_size):
    id_list = []
    item_dict_list = []
    for page in range(page_size):
        url = 'http://2382.bd.aiyichuan.com/wap/Act/b2c_ajax?type=best_selling&page=' + str(page + 1)
        data = common_method_get(url).do_get()

        data_list = data['list']
        for item_data in data_list:
            item_dict = {}
            spu_id = item_data['id']
            id_list.append(spu_id)
            item_dict[str(spu_id)] = item_data
            item_dict_list.append(item_dict)

    id_set = set(id_list)
    id_list_new = list(id_set)
    id_list_new.sort()
    return id_list_new, item_dict_list


if __name__ == '__main__':
    # id_list_new, item_dict_list = get_item_list(page_size)
    # print('id_list_new###len=', len(id_list_new), '数据=', id_list_new)
    # print('item_dict_list###len=', len(item_dict_list), '数据=', item_dict_list)

    site_id=11001
    page_size = 10
    data_list = []
    prefix_file_name = 'D:\\project\\python\\站点数据\\上海站\\'

    shop_data_list = []
    shop_file_path = prefix_file_name + '最新商品门店_page_70.csv'

    item_data_list = []
    item_file_path = prefix_file_name + '最新爬取商品明细_page_70.csv'

    # item_class = get_item_class(data_list, goods_category_id_dict, shop_category_id_dict, shop_center_id_dict, headers,
    #                             page_size, shop_file_path, item_file_path)
    # item_class.write_item()

    # # 保存门店数据到数据库
    # shop_class_database = save_shop_class(host, user, passwd, database, shop_center_id_dict, site_id, shop_file_path)
    # shop_class_database.save_shop_data()
    #
    # # 保存商品数据到数据库
    # item_class_database = save_item_class(host, user, passwd, database, site_id, item_file_path)
    # item_class_database.save_item_data()
