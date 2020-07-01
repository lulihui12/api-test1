from time import sleep

from selenium.webdriver.common.by import By

from seleniumtest2.page.add_member import AddMember
from seleniumtest2.page.basepage import BasePage


class Add2(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def addnumber(self):
        self.find(By.ID,"menu_contacts").click()
        def wait_for(driver):
            #判断是否存在下个页面的元素
            ele_len = len(self.finds(By.ID,"username"))
            #如果不存在，则点击那个按钮
            if ele_len < 1:
                self.find(By.CSS_SELECTOR,".js_has_member>div:nth-child(1) .js_add_member").click()
            #如果username存在，就返回true
            return ele_len >= 1
        self.wait(wait_for)
        return AddMember(reuse=True)