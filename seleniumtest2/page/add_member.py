from time import sleep

from selenium.webdriver.common.by import By

from seleniumtest2.page.basepage import BasePage


class AddMember(BasePage):
    def add_member(self):
        #   self.driver.find_element_by_name("username").send_keys("测试同学小慧")
        self.find(By.NAME, "username").send_keys("测试同学小慧")
        self.find(By.NAME, "english_name").send_keys("test123")
        self.find(By.ID,"memberAdd_acctid").send_keys("11231121")
        self.find(By.NAME, "mobile").send_keys("15943346480")

        sleep(5)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()


#   self.driver.find_element_by_name("english_name").send_keys("teststudent")
#   self.driver.find_element_by_name("acctid").send_keys("19921212")
#   #self.driver.find_element_by_xpath("//*[@id='js_upload_file']/div/div[1]").click()
#   #self.driver.find_element_by_xpath("//*[@id='__dialog__avatarEditor__']/div/div[2]/div/div[1]/div[2]/a/input").send_keys("/Users/lulihui/Downloads/test.jpeg")
#   sleep(5)
#   #self.driver.find_element_by_xpath("//*[@id='__dialog__avatarEditor__']/div/div[3]/a[1]").click()
#   self.driver.find_element_by_name("mobile").send_keys("15943346480")
# #  sleep(5)
# #  self.driver.find_element(By.CSS_SELECTOR,"#js_contacts56 > div > div.member_colRight > div > div:nth-child(4) > div > form > div.member_edit_formWrap > div:nth-child(1) > div.member_edit_item.member_edit_item_Radios > div.member_edit_item_right > label:nth-child(2) > input").click()
#   sleep(5)
#   self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()


    def get_first(self):
        sleep(5)
       #return self.find(By.CSS_SELECTOR, "#member_list tr:nth-child(1) td:nth-child(2)").get_attribute("title")
        eles=self.finds(By.CSS_SELECTOR,"#member_list td:nth-child(2)")
       #对所有元素进行遍历，获取其title属性，追加到列表中

        ele_list=[]
        for ele in eles:
           ele_list.append(ele.get_attribute("title"))
        return ele_list