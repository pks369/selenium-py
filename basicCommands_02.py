'''
basic webdriver commands

capture title of the pag

captue url of the page

closing and quiting browser

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
#parent url
driver.get('http://demo.automationtesting.in/Windows.html')
print(driver.title) # title of page
print(driver.current_url) #return url of the page    click
#open 2 browser
#child url
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click() # inspect click & copy/ copy XPath
time.sleep(5)
# driver.close() # close parent url
# driver.quit()  # quit all url like parent,child
