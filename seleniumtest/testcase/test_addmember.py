from seleniumtest.page.index import index


class Test_add:
    def setup(self):
        self.index=index()
    def test_addmember(self):
        add_member=self.index.go_to_add_member()
        add_member.add_member()
        assert add_member.get_first() == "测试同学小慧"
        # self.index.go_to_add_member().add_member()
        # test=self.index.go_to_add_member().get_first()
        # assert test == "测试同学小慧"

