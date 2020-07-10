from selenium.webdriver.common.by import By

from page.basepage import BasePage
from page.register import Register


class Login(BasePage):
    def scan(self):
        pass
    def login(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self._driver)
