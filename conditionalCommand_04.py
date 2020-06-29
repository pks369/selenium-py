'''
Conditional  commands
is_dispalyed()
is_enabled()
is_selected()
'''
from selenium import  webdriver
# import  time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

driver.get('http://newtours.demoaut.com/')

user_ele=driver.find_element_by_name('userName')
print(user_ele.is_displayed()) # return true/false based of the element status
print(user_ele.is_enabled()) # return true /false

pass_ele=driver.find_element_by_name('password')
print(pass_ele.is_displayed()) # return true/false based of the element status
print(pass_ele.is_enabled()) # return true /false

user_ele.send_keys('mercury')
pass_ele.send_keys('mercury')
driver.find_element_by_name('login').click()

roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
print("staus of round trip radio button:",roundtrip_radio.is_selected()) #status of radio button round trip

oneway_radio=driver.find_element_by_css_selector("input[value=oneway]")
print("staus of one trip radio button:",oneway_radio.is_selected()) #status of radio button one trip
