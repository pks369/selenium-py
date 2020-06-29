'''
wait statement

imlictly_wait : Implicit wait is also referred to as dynamic wait.
                If it does not find the element in the
                specified duration, it throws ElementNotVisibleException.

                It is by default applied to all the elements in the script.
                We cannot wait based on a specified condition like element selectable/clickable unlike explicit.
                It is usually used when you are sure the element may be visible in a certain time.
'''
from selenium import  webdriver
# import  time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
driver.get('http://newtours.demoaut.com/') #opening url takes some time

#wait some time here
driver.implicitly_wait(10)  #second wait for all elements
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()