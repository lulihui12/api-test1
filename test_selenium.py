# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class Test123:
#     def setup(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get("https://www.baidu.com/")
#         self.driver.implicitly_wait(5)
#     def teardown(self):
#         self.driver.quit()
#
#     def testbaidu(self):
#         self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
#         self.driver.find_element(By.XPATH,'//*[@id="su"]').click()
#
#         #self.driver.find_element(By.XPATH,'//*[@class="opr-recommends-merge-content"]/div[1]/a/span').click()
#
#         #self.driver.find_element(By.XPATH,'//*[@class="c-gap-left-small c-icon opr-toplist1-icon"]').click()
#         sleep(10)
#         self.driver.find_element(By.CSS_SELECTOR, '[id=page] a:nth-last-child(2)').click()
#         sleep(5)
#         self.driver.find_element(By.CSS_SELECTOR,'[id=u]>a:nth-child(2)').click()
#         sleep(6)
#         self.driver.find_element(By.CSS_SELECTOR,'[id=u]>div a:nth-child(2)').click()
#         sleep(5)
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test123:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()    #窗口最大化
    def teardown(self):
        self.driver.quit()

    def testcase(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        elemenet_click =self.driver.find_element(By.CSS_SELECTOR,'[value="click me"]')
        elemenet_dblclick = self.driver.find_element(By.CSS_SELECTOR,'[value="dbl click me"]')
        elemenet_rightclick = self.driver.find_element(By.CSS_SELECTOR,'[value="right click me"]')
        action=ActionChains(self.driver)
        action.click(elemenet_click)    #元素点击
        action.double_click(elemenet_dblclick)   #元素双击
        action.context_click(elemenet_rightclick)    #鼠标右键
        sleep(5)
        action.perform()
        sleep(5)

    def testmoveelement(self):
        self.driver.get("https://www.baidu.com/")
        ele=self.driver.find_element_by_id("s-usersetting-top")
        action=ActionChains(self.driver)
        action.move_to_element(ele)       #将光标移动到设置上
        action.perform()
        sleep(5)

    def testdrag(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag=self.driver.find_element_by_id("dragger")
        tomove=self.driver.find_element_by_xpath("/html/body/div[4]")
        action=ActionChains(self.driver)
        action.drag_and_drop(drag,tomove)  #将drag元素拖拽到moveto元素位置
        #action.click_and_hold(drag).release(tomove).perform()  #另一种方法，点击按住不放，moveto下一个元素，再release
        #ActionChains(self.driver).drag_and_drop(drag,tomove).perform()  #方法一的分布式写法
        action.perform()
        sleep(5)


    def testkeys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element1=self.driver.find_element_by_xpath("/html/body/label[1]/input")
        action=ActionChains(self.driver)
        action.click(element1)
        sleep(5)
        action.send_keys("username").pause(1)    #输入uesrname；pause 暂停
        action.send_keys(Keys.SPACE).pause(1)    #输入空格，pause
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(2)    #删除一位 pause
        action.send_keys(Keys.BACK_SPACE).pause(2)       #再删除一位
        sleep(5)
        action.perform()
