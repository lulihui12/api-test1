import requests


class BaseApi:
    def send_api(self,req:dict):#传入一个值req  可能是字典的格式
        #使用request完成多请求的构造，根据method动态改变 get、put、post
        return requests.request(**req).json()