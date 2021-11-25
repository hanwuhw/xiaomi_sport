import os,time,random
from selenium import webdriver
#ss让人
driver = webdriver.Edge()
driver.set_window_position(20,40)
driver.set_window_size(1100,700)
xzy_stems_num = random.randint(30000,40000) #生成步数随机数
hwj_stems_num = random.randint(30000,40000) #生成步数随机数

driver.get("http://sport.hanwuwj.top")# 打开一个页面（登录页）
########肖正阳登录#############
eleUser = driver.find_element_by_xpath("/html/body/div/form/div[1]/div/input")# 获取用户名
elePwd = driver.find_element_by_xpath("/html/body/div/form/div[2]/div/input")# 获取密码元素节点
elestep = driver.find_element_by_xpath("/html/body/div/form/div[3]/div/input")# 获取步数节点
eleUser.send_keys("17634417027") # 写入用户名
elePwd.send_keys("Xzy1126632753") # 写入密码
elestep.send_keys(xzy_stems_num) #写入步数
time.sleep(2)
login_Button = driver.find_element_by_css_selector("button") #获取提交按钮
login_Button.click()  # 点击登录按钮
time.sleep(2)
#########胡文君登录#############
eleUser = driver.find_element_by_xpath("/html/body/div/form/div[1]/div/input")# 获取用户名
elePwd = driver.find_element_by_xpath("/html/body/div/form/div[2]/div/input")# 获取密码元素节点
elestep = driver.find_element_by_xpath("/html/body/div/form/div[3]/div/input")# 获取步数节点

eleUser.clear(),elePwd.clear(),elestep.clear() #清除输入框
eleUser.send_keys("18338607710") #写入用户名
elePwd.send_keys("HWJ123456") # 写入密码
elestep.send_keys(hwj_stems_num) #写入步数
time.sleep(2)
login_Button = driver.find_element_by_css_selector("button")
login_Button.click()  # 点击登录按钮
time.sleep(2)
driver.close()
driver.quit()
print("刷步数成功，感谢您的使用！")

