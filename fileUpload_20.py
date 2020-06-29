'''
Agenda
   file Upload:
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

driver.maximize_window()#Maxmize window size
driver.get("https://testautomationpractice.blogspot.com/")
# driver.switch_to.window(0)

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users//Dell//Pictures//circular.png")









