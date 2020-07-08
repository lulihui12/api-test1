import requests


class TestmemberApi:
    secrete = "LYCT9hnHtwA0qx9cbzxQAh1Lwt4lkYF2UPS_qefWHuM"
    id = 'wwe74f5c4f4abd49bf'

    def setup(self):
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secrete}')
        self.token = r.json()['access_token']

    def test_api(self):
        # 查询这个userid是否存在，如存在删除；不存在新建
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=11231121")
        if r.json()["errcode"] == 0:
            r = requests.get(
                f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=11231121")
            print(r.json())
        payload = {
            "userid": "11231121",
            "name": "test12345",
            "mobile": "13381037765",
            "department": [1, 2]
        }
        # 传参必须为json格式，使用json=payload  实现字典格式转换json   或者直接  json.dumps()  序列化
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}", json=payload)
        print(r.json())
        # 修改接口
        payload = {
            "userid": '11231121',
            "name": "测试同学慧"
        }
        # 传参必须为json格式，使用json=payload  实现字典格式转换json   或者直接  json.dumps()  序列化
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}", json=payload)
        print(r.json())
