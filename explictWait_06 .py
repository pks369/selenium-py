'''
wait statement
Explicit wait: It is applicable to only a certain element which is specific to a certain condition.
               In explicit, we can specify the wait based on a specific condition.
               It is usually used, when you are not aware of the time of the element visibility.
               It is subjected to dynamic nature.
'''
from selenium import  webdriver
from selenium.webdriver.common.by import By
import  time
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
driver.maximize_window()
driver.get('https://www.expedia.com/') #opening url

# driver.find_element_by_id('tab-flight-tab-hp').click()
driver.find_element(By.ID,'tab-flight-tab-hp').click() # flight button

driver.find_element(By.ID,'flight-origin-hp-flight').send_keys("SFO") #origin
# time.sleep(2) # from python in like java thread.sleep

# driver.find_element(By.ID,'flight-destination-hp-flight').send_keys("NYC") # destination

# driver.find_element(By.ID,"section-flight-tab-hp-flight").clear()



# driver.find_element(By.ID,"section-flight-tab-hp-flight").send_keys("2/6/2020")

# driver.find_element(By.ID,"section-flight-tab-hp-flight").send_keys("6/6/2020")

# driver.find_element_(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button/span").click()



