'''
Agenda
   Capture screen shot:
'''
from selenium import  webdriver
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')

driver.maximize_window()#Maxmize window size
driver.get("http://newtours.demoaut.com/mercurywelcome.php")

driver.save_screenshot('C:\\Users\\Dell\\PycharmProjects\\selenium\\data\\secreenshot\\homepage.png ')

# driver.get_screenshot_as_file('C:\\Users\\Dell\\PycharmProjects\\selenium\\data\\homepage1.jpg ')








