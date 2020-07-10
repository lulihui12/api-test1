from selenium import  webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    #driver要指定类型,python才能识别到
    def __init__(self,driver:WebDriver=None):  #给变量定义一个类型   webdriver，没有实质作用
        #r=让python编译器知道有一个实例变量driver
        self.driver=None
        if driver is None:
            #如果发现driver是空，则复用已有的浏览器
            opts=webdriver.ChromeOptions()
            opts.debugger_address="127.0.0.1:9222"
            self.driver=webdriver.Chrome(options=opts)
            #隐式等待，解决元素加载过慢的问题
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver

