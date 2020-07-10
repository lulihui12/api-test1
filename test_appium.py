# from time import sleep
#
# from appium import webdriver  # 导入appium
#
# desire_cap = {
#     "platformName": "Android",
#     "deviceName": "emulator-5554",
#     "appPackage": "com.xueqiu.android",
#     "appActivity": ".view.WelcomeActivityAlias",
#     "noReset":"true",   #是否在测试前后重置相关环境
#     "dontStopAppOnReset":"true",  #首次启动的时候，不停止app   可以调试或运行的时候提升速度
#     "skipDeviceInitialization":"true"    #跳过安装、权限设置
# }
# # 启动appium server时，会在本地4723端口监听；/wd/hub 为固定地址
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
# # 方便查找元素 隐式等待
# driver.implicitly_wait(10)
# driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()   #点击搜索按钮
# driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")    #搜索框输入alibaba
# driver.back()  #返回到上一页
# driver.back()
# sleep(5)    #强制等待
# driver.quit()


#列表元素求和
list=[1,2,3,4,5,6]
def sum(list):
    if list==[]:
        return 0
    return list[0]+sum(list[1:])
a=sum(list)
print(a)

#求列表元素个数
list=[1,2,3,4,5,6,7,8]
def count(list):
    if list==[]:
        return 0
    return 1+count(list[1:])
b=count(list)
print(b)

#求列表元素最大值
list=[7,3,6,1]
def max(list):
    if len(list)==2:
        return list[0] if list[0]>list[1] else list[1]
    sub_max=max(list[1:])
    return list[0] if list[0]>sub_max else sub_max
c=max(list)
print(c)