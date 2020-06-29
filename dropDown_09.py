'''
Agenda:
1.)Select one option: 3 approaches
2.)Count how many option present :4
3.)Capture options from drop  down value :morning.afternoon,evening

'''

from selenium import  webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?')

sel_drp= Select(driver.find_element_by_id('RESULT_RadioButton-9'))
# print(type(sel_drp))

#select by visble text
#sel_drp.select_by_visible_text('Morning') # Morning

#select by index
#sel_drp.select_by_index(2) #Afternoon

# select by value
#sel_drp.select_by_value('Radio-2') # Evening

# print(len(sel_drp.options))  # Count no. of options 4



# Capture all the options & print them as output
all_options=sel_drp.options
# print(type(all_options))
for option in all_options:
 # print(option.text) # all text
  if option.text=='Morning':
     break;
print(option.text) # only one text based on text  like Morning,Afternoon,Evening



