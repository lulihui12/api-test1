from seleniumtest2.page.index import index


class Test_add:
    def setup(self):
        self.index=index(reuse=True)
    def test_addmember(self):
        add_member=self.index.go_to_add_member()
        add_member.add_member()
        assert "测试同学da慧" in add_member.get_first()
        # self.index.go_to_add_member().add_member()
        # test=self.index.go_to_add_member().get_first()
        # assert test == "测试同学小慧"

