from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url=""     #定义一个  _base_url 初始值为空

    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self._driver=webdriver.Chrome()
        else:
            self._driver=driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,locator):      #定义find函数，元素定位，方便后续调用
        return self._driver.find_element(by,locator)