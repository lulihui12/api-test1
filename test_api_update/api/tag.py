


from test_api_update.api.wework import WeWork
from test_api_update.api.base_api import BaseApi


class Tag(BaseApi):
    secret='GUKKxigux3vmCdYeiV9hQiSYoDRguvcD4nNX9rsbpbk'
    #token公用，创建一个init初始化
    def __init__(self):
        self.token=WeWork().get_token(self.secret)
    def add(self,name):
        data ={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params":{
                "access_token":self.token
            },
            "json":{
                "group_name": "大客户专用",
                "tag": [{
                    "name": name
                }
                ]
            }
        }
        return self.send_api(data)

    def get_tag(self):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params":{
                "access_token": self.token
            },
            "json":{
                "tag_id":[]
            }
        }
        return self.send_api(data)

    def del_tag(self,tag_id):
        data={
            "method":'post',
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params":{
                "access_token": self.token
            },
            "json":{
                "tag_id": [tag_id]
            }
        }
        return self.send_api(data)

    def update_tag(self,id,name):
        data={
            "method":'post',
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params":{
                "access_token":self.token
            },
            "json":{
                "id": id,
                "name": name,
                "order": 1

            }
        }

        return self.send_api(data)
