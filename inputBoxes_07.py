'''
Agenda
Working with input boxes

we will cover following operations.
1.)How to find how many input boxes present in web page.
2.)How to provide value into text box
3.)How to get status of text box  like enable/disable

'''
from selenium import  webdriver
from  selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?')
inputBoxes=driver.find_elements(By.CLASS_NAME,'text_field')
# inputBoxes=driver.find_elements(by=By.CLASS_NAME,value='text_field')
print(len(inputBoxes)) # no. of input boxes 6

status=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("Display or not status is:",status) # True/False

status=driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print("Enable or not status is :",status) # True/False

driver.find_element(by=By.ID,value='RESULT_TextField-1').send_keys('Pappu') #locator

driver.find_element(By.ID,'RESULT_TextField-2').send_keys('Singh') # filled all input boxes

driver.find_element_by_id('RESULT_TextField-3').send_keys('8983356084')

driver.find_element_by_id('RESULT_TextField-4').send_keys('India')

driver.find_element_by_id('RESULT_TextField-5').send_keys('Bangalore')

driver.find_element_by_id('RESULT_TextField-6').send_keys('pappu.singh@girmiti.com')

