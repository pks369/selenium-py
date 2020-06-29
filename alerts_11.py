'''
Agenda:
alerts button
1.)closes alert  window using ok button
2.)closes alert  window using cancel button
'''
from selenium import  webdriver
import  time

driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
driver.get('https://testautomationpractice.blogspot.com/')
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
driver.switch_to_alert().accept() # closes alert  window using ok button
# driver.switch_to_alert().dismiss() # closes alert  window using cancel button
