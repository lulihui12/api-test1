from page.main import Main


class TestRister():
    def setup(self):
        self.main=Main()
    def test_register(self):
        assert self.main.goto_register().register()
