'''
Agenda
   Excel operations:

'''
import xlutils
from selenium import  webdriver
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
driver.maximize_window()#Maxmize window size
driver.get("http://newtours.demoaut.com/")
path="C:\\Users\\Dell\\PycharmProjects\\selenium\\data\\login.xlsx"

rows= xlutils.getRowCount(path,'Sheet1')
for r in range(2,rows+1):
   username= xlutils.readData=(path,'Sheet1',r,1)
   password= xlutils.readData=(path,'Sheet1',r,2)

   driver.find_element_by_name('login').click()

   if driver.title=="Find a Flight:Mercury Tours:":
       print("test is passed")
       xlutils.writeData(file,"Sheet1",r,3,"test is passed")
   else:
       print("test is failed")
       xlutils.writeData(path,"Sheet1",r,3,"test failed")











