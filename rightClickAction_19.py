'''
Agenda
   Mouse Actions:
   3.)Right Click

'''
from selenium import  webdriver
from  selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()#Maxmize window size
button=driver.find_element_by_xpath("/html/body/div[1]/section/div/div/div/p/span")
actions=ActionChains(driver)
actions.context_click(button).perform() #Mouse  right click action








