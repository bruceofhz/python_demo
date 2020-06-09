import pymysql
import requests
from urllib3 import encode_multipart_formdata


class upload_file:
    def __init__(self, img_path, img_name, pic_url):
        self.img_path = img_path
        self.img_name = img_name
        # 网络上的图片地址
        self.pic_url = pic_url

    # 图片下载
    def down_load(self):
        pic_url = self.pic_url
        content = requests.get(pic_url).content

        file_name = self.img_path + self.img_name
        with open(file_name, 'wb') as f:
            f.write(content)

    # 文件上传
    def send_file(self):
        url = 'https://imgsrc.ishanshan.com/gimg/upload'
        with open(self.img_path + self.img_name, 'rb') as f:
            file = {
                "file": (self.img_path, f.read()),  # 引号的file是接口的字段，后面的是文件的名称、文件的内容
                "key": "value",  # 如果接口中有其他字段也可以加上
            }
            encode_data = encode_multipart_formdata(file)
            file_data = encode_data[0]
            headers_from_data = {
                "Content-Type": encode_data[1]
            }
            # 'Content-Type': 'multipart/form-data; boundary=c0c46a5929c2ce4c935c9cff85bf11d4',这里上传文件用的是form-data,不能用json

            response = requests.post(url=url, headers=headers_from_data, data=file_data).json()
        return response

    def deal_with_file(self):
        upload_file.down_load(self)
        response = upload_file.send_file(self)
        result = ''
        if 'sucess' in response:
            result = response['url']
        return result

    def deal_with_spu(self):
        site_id = 11000
        host = '192.168.1.52'
        user = 'jpss'
        passwd = 'Jpss541018!'
        database = 'hbsitedb'

        spu_dict_list = {}
        sql = "select id,cover,imgs,poster_img from goods_spu spu where deleted =0  and site_id =" + str(site_id)
        conn = pymysql.connect(host=host,
                               user=user,
                               passwd=passwd,
                               db=database)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            spu_id = data[0]
            spu_dict_list[str(spu_id)] = data
        cursor.close()
        conn.close()
        return spu_dict_list

    def update_spu(self):
        site_id = 11000
        host = '192.168.1.52'
        user = 'jpss'
        passwd = 'Jpss541018!'
        database = 'hbsitedb'

        spu_dict_list = {}
        sql = "update goods_spu set cover= '++'where deleted =0  and site_id =" + str(site_id)
        conn = pymysql.connect(host=host,
                               user=user,
                               passwd=passwd,
                               db=database)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            spu_id = data[0]
            spu_dict_list[str(spu_id)] = data
        cursor.close()
        conn.close()
        return spu_dict_list


if __name__ == '__main__':
    # 图片路径
    img_path = 'C:\\Users\\Administrator\\Desktop\\pic\\'
    # 图片名称
    img_name = '20190816/1565947987400.gif'

    pic_url = 'http://q6.img.aiyichuan.com/urm_huodong/20190912/1568280797777.jpg?imageView2/1/w/750/h/750'
    # result = upload_file(img_path, img_name, pic_url).deal_with_file()
    # print(result)

    spu_dict_list = upload_file(img_path, img_name, pic_url).deal_with_spu()

    pic_dict_list = {}
    for spu_id in spu_dict_list:
        spu_data = spu_dict_list[str(spu_id)]
        # print(spu_data)

        path = 'C:\\Users\\Administrator\\Desktop\\pic\\'
        name = str(spu_id) + '.gif'
        url = spu_data[1]
        result = upload_file(path, name, url).deal_with_file()

        pic_dict_list[str(spu_id)] = result

        site_id = 11000
        host = '192.168.1.52'
        user = 'jpss'
        passwd = 'Jpss541018!'
        database = 'hbsitedb'

        sql = 'update goods_spu set cover=\"' + str(result) + '\" where deleted =0  and site_id =' + str(
            site_id) + ' and id=' + str(spu_id) + ';'
        print(sql)
