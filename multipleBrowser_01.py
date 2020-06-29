# Run test on chrome,firefox,ie
from selenium import webdriver
# import time
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')


driver.get('https://www.google.com')
driver.maximize_window()
#driver.minimize_window()
print(driver.title) # title of page
# time.sleep(100000)
print(driver.current_url) #return url of the page
# print(driver.page_source)  # html code for the page
# driver.close()  # close the browser