import requests

from test_api.api.base_api import BaseApi


class WeWork(BaseApi):
    # 获取token
    corpid='wwe74f5c4f4abd49bf'

    def get_token(self,secret):
        data={
            "method":'get',
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params":{
                "corpid":self.corpid,
                "corpsecret":secret
            }
        }
        return self.send_api(data)['access_token']  #**tata 解包:满足必填字段的需求，无限扩展
