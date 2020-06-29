'''
Agenda
Work wih table
  1.)count no of rows
  2.)count no of cols
  3.)count all  table
'''
from selenium import  webdriver
from  selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')

driver.get("C:\\Users\\Dell\\PycharmProjects\\selenium\\data\\sample.html")
rows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr")) # count no of rows
cols=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th")) # count no of cols
print("no. of rows:",rows,'\n'"no. of cols:",cols)
# /html/body/table/tbody/tr[2]/td[1]
# /html/body/table/tbody/tr[3]/td[2]
print("Product"+"  "+"Article"+"  "+"Price")
for r in range(2,rows+1): # first is header row
    # print('row',r)
    for  c in range(1,cols+1):
      # print('col',c)
       value=driver.find_element_by_xpath("/ html / body / table / tbody / tr["+str(r)+"]/ td["+str(c)+"]").text
       print(value,end= ' ') # p1  00001  10
    print()