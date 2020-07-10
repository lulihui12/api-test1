from seleniumtest.page.add_member import AddMember
from seleniumtest.page.basepage import BasePage


class index(BasePage):
    def go_to_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap").click()
        return AddMember(self.driver)

    def import_address(self):
        pass

    def add_number(self):
        pass
