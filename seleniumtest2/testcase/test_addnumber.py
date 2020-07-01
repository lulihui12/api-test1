from seleniumtest2.page.index_gotoadd import Add2


class Test123:
    def setup(self):
        self.Add2 = Add2(reuse=True)

    def test123(self):
        add_memeber = self.Add2.addnumber()
        add_memeber.add_member()
        assert "测试同学小慧" in add_memeber.get_first()
