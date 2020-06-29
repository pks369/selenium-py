from selenium import  webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver import ActionChains



driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()#Maxmize window size
element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions=ActionChains(driver)
actions.double_click(element).perform() #Double click on button