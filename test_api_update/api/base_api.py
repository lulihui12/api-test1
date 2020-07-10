import requests
from jsonpath import jsonpath


class BaseApi:
    def send_api(self, req: dict):  # 传入一个值req  可能是字典的格式
        # 使用request完成多请求的构造，根据method动态改变 get、put、post
        print(req)
        r=requests.request(**req)
        print(r.json)
        return r.json()

    @classmethod
    def get_jsonpath(cls, json, expr):
        return jsonpath(json, expr)
        #ag_id = jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="hello")].id')
