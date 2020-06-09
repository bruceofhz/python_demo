import json

import requests



# site_data_list=[{1: '上海站'}, {2: '广州站'}, {3: '北京站'}, {4: '深圳站'}, {5: '苏州站'}, {6: '杭州站'}, {7: '南京站'}, {8: '厦门站'}, {9: '成都站'}, {10: '宁波站'}, {11: '重庆站'}, {12: '珠海站'}, {13: '武汉站'}, {14: '长沙站'}, {15: '郑州站'}, {16: '沈阳站'}, {17: '海口站'}]
# b2c_cats=[{'id': 29, 'name': '美食'}, {'id': 16, 'name': '休闲娱乐'}, {'id': 9, 'name': '丽人'}, {'id': 27, 'name': '亲子教育'}, {'id': 35, 'name': '周边游'}, {'id': 36, 'name': '生活服务'}]

class site_class:
    def __init__(self,headers):
        self.headers=headers


    def get_index_site(self):
        url = 'http://2382.bd.aiyichuan.com/wap/Act/index'
        response = requests.get(url, headers=self.headers)
        text = response.content.decode()

        json_text = json.loads(text)
        data = json_text['data']

        locations = data['locations']

        # 分类cat_id
        b2c_cats=  data['b2c_cats']

        site_data_list=[]
        for current_site in locations:
            id = current_site['id']
            name = current_site['name']

            site_data_dict = {}
            site_data_dict[id] = name
            site_data_list.append(site_data_dict)
        return site_data_list, b2c_cats




