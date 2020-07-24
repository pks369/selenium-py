from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
driver.maximize_window()
driver.get('http://newtours.demoaut.com/') #opening url
print(driver.title) # title of page


import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="login"
)
cur =db.cursor()

cur.execute("SELECT * FROM users")
cols = cur.fetchall()
for col in cols:
     driver.find_element_by_name('userName').send_keys(col[0])
     driver.find_element_by_name('password').send_keys(col[1])
     driver.find_element_by_name('login').click()
     time.sleep(5)

     # validatuiion
     if driver.title == "Find  A  Flight: Mercury Tours: ":
       print('Test passed')
     else:
       print('Test failed')
     driver.find_element_by_link_text("Home").click()

cur.close()
db.close()
print('Data Driven Test Completed')



