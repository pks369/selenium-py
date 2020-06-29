'''
Agenda:
Working with frame:
                 1.)switch_to.frame(name)
                 2.)switch_to.frame(id)
'''
from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
driver.maximize_window()
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageFrame") # first frame
driver.find_elements_by_link_text("org.openqa.selenium").click()

# driver.switch_to_default_content() #main page
#
# driver.switch_to_frame("packageFrame") #second frame
# driver.find_elements_by_link_text('webDriver').click()
# driver.switch_to_default_content()
# time.sleep(3)
#

driver.switch_to_default_content()
driver.switch_to_frame("classFrame") #third frame
time.sleep(3)
driver.find_elements_by_link_text('webDriver').click()
driver.find_element_by_xpath("/html/body/div[4]/ul[1]/li/table/caption/span[1]").click()
driver.switch_to_default_content()


