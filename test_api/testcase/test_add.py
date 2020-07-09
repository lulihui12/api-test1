#-*- coding:utf-8 -*-
import json

from jsonpath import jsonpath

from test_api.api.tag import Tag


class TestTag:
    def setup(self):
        self.tag=Tag()

    #实现增删改查
    def test_all(self):
        tag_id=jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="hello")].id')#使用jsonpath：取出name为hello的id：首先找个一个字段tag (tag下的三个值不是他的子节点，就是他的值)；通过属性name进行过滤
        if  tag_id:
            self.tag.del_tag(tag_id[0])
        self.tag.add("hello")
        tag_id=jsonpath(self.tag.get_tag(), '$..tag[?(@.name=="hello")].id')[0]
        self.tag.update_tag(tag_id,"hahahahaha123")



    def test_add(self):
       # self.tag.add("张三")
       # self.tag.add("李四")
       self.tag.add("hello")
       tags=self.tag.get_tag()
       if "hello" in jsonpath(tags,"$..name"):
           self.tag.del_tag(jsonpath(tags,'$..tag[?@.name=="hello"]'))
       # print(self.tag.get_tag()["tag_group"][0]["tag"][0]["name"])  #比较low的方法

    def test_get(self):

        print(json.dumps(Tag().get_tag(),indent=2))   #美化格式

    def test_del(self):
        print(Tag().del_tag('etm3FVCwAANLJa5XkPY6WQii1eIgeHNA'))

    def test_update(self):
        print(Tag().update_tag('etm3FVCwAAbiwC1Ncr11t0rHk2erh1-g',"改成功了么"))
