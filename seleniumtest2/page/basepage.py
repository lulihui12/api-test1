from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = ""
    driver = ""

    def __init__(self, reuse=False):  # 是否复用浏览器
        if reuse == True:
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, location):    #封装find_element方法
        return self.driver.find_element(by, location)
    def finds(self,by,location):
        return self.driver.find_elements(by,location)