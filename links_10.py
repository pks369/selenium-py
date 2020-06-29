'''
Agenda:
1.)Print how many links present in  a page
2.)Print all link in console using loop(Extract all link)
3.)Clicking on the link

'''

from selenium import  webdriver
from  selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
# driver.get('https://fs2.formsite.com/meherpavan/form2/index.html')
driver.get('http://newtours.demoaut.com/')
driver.get('https://www.girmiti.com/')
    
links=driver.find_elements(By.TAG_NAME,'a')

# print("No. of links present:",len(links))

# for link in links:
#    print(link.text)

#Clicking on the link
# driver.find_element(By.LINK_TEXT,'REGISTER').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'R').click()