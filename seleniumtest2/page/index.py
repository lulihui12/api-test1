from selenium.webdriver.common.by import By

from seleniumtest2.page.add_member import AddMember
from seleniumtest2.page.basepage import BasePage


class index(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def go_to_add_member(self):
        #self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #elf.find(".index_service_cnt_itemWrap").click()
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap").click()

        return AddMember(reuse=True)


