from time import sleep

from selenium.webdriver.common.by import By

from seleniumtest2.page.add_member import AddMember
from seleniumtest2.page.basepage import BasePage


class Add2(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def addnumber(self):
        self.find(By.ID,"menu_contacts").click()
        sleep(5)
        self.find(By.CSS_SELECTOR,".js_has_member>div:nth-child(1) .js_add_member").click()
        return AddMember(reuse=True)