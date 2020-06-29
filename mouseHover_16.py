'''
Agenda
   Mouse Actions:
  1.)Mouse Hover
  2.)Double Click
  3.)Right Click
  4.)Drag & Drop

'''
from selenium import  webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()#Maxmize window size
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys('Admin')
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys('admin123')
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermgnt=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actiions=ActionChains(driver)
actiions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()





