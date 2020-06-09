import json

import requests

from 站点 import config


class common_method_get:
    def __init__(self, url, headers):
        self.url = url

        if None is headers:
            self.headers = config.headers
        else:
            self.headers = headers

    def do_get(self):
        response = requests.get(self.url, headers=self.headers)
        text = response.content.decode()

        json_text = json.loads(text)
        data = json_text['data']
        return data




class common_method_post:
    def __init__(self, url, headers, post_body):
        self.url = url

        if None is headers:
            self.headers = config.headers
        else:
            self.headers = headers

        self.post_body = post_body

    def do_post(self):
        response = requests.post(self.url, self.post_body, headers=self.headers)
        text = response.content.decode()

        json_text = json.loads(text)
        data = json_text['data']
        return data
