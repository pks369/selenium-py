'''
Redirect  one url to another url like Forward & Backward

Thread.sleep() in java:
time.sleep(): It does not wait for the complete duration of time. In case it finds the element before the
                duration specified, it moves on to the next line of code execution, thereby reducing the time
                of script execution.
'''

from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

driver.get('https://www.python.org/')
print(driver.title) #FW

driver.get('https://www.selenium.dev/')
# time.sleep(5)
print(driver.title) #BW

driver.back()        #FW
# time.sleep(5)
print(driver.title)  #FW


driver.forward()     #BW

print(driver.title)  #BW



