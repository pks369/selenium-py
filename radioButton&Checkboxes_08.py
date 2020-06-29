'''
Agenda:
Working with radio button & check boxes.
1.) check radio button & check box   is selected  or not : isSelected()
2.) Click radio button & checkbox
'''
from selenium import  webdriver
from  selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?')
status=driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
print("Radio button status is:",status) # False


driver.find_element_by_css_selector("[for='RESULT_RadioButton-7_0']").click() # selected radio button

status = driver.find_element_by_css_selector("[name='RESULT_RadioButton-7']").is_selected()
print("Radio button status is:",status,'\n') #True





status=driver.find_element_by_id('RESULT_CheckBox-8_0').is_selected()
print("Check box status is:",status) # False


driver.find_element_by_css_selector("[for='RESULT_CheckBox-8_0']").click() # selected check box

# driver.find_element_by_css_selector("[for='RESULT_CheckBox-8_6']").click() # selected check box


status=driver.find_element_by_id('RESULT_CheckBox-8_0').is_selected()
print("Check box status is:",status) #True



