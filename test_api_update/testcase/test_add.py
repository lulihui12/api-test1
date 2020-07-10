#-*- coding:utf-8 -*-
import pytest

from test_api_update.api.tag import Tag
from test_api_update.api.base_api import BaseApi



class TestTag:
    #setup 对核心对象的初始化
    @classmethod
    def setup_class(cls):    #cls 当所有测试用例执行的时候，setup只执行一次；而tag只初始化一次就可以
        cls.tag=Tag()
        data=cls.tag.get_tag()
    #     for name in ["api","zhangsan"]:
    #         tag_id=cls.tag.get_jsonpath(data,f'$..tag[?(@.name=="{name}")].id')
    #      # 使用jsonpath：取出name为hello的id：首先找个一个字段tag (tag下的三个值不是他的子节点，就是他的值)；通过属性name进行过滤
    #         if tag_id:
    #             cls.tag.del_tag(tag_id[0])
    # #def setup(self):        #setup 每次执行测试用例的时候，都会执行一次
    # #   self.tag=Tag()

    #实现增删改查
    @pytest.mark.parametrize("name_old,name_new",[
        ("haha", "test1"),
        ("xiaowang", "test2"),
        ("hello","test3"),
        ("didi","test4")
    ])
    def test_all(self,name_old,name_new):
        data=self.tag.get_tag()
        for name in [name_old,name_new]:
            tag_id=self.tag.get_jsonpath(data,f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                self.tag.del_tag(tag_id[0])

        assert self.tag.add(name_old)["errcode"]==0
        tag_id=self.tag.get_jsonpath(self.tag.get_tag(), f'$..tag[?(@.name=="{name_old}")].id')[0]
        assert self.tag.update_tag(tag_id,name_new)["errcode"]==0



