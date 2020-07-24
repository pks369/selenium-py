'''
Agenda:
Python Unit test  HTML TestRunner Reports
Selenium  Python Test Case using Unit Test,HTML Reports
Selenium Python Project |Unit Test, POM|,HTML REports

# pip install html-testRunner

#Test case:OrangeHRM login test
1.)Launch  browser:one time activity
2.)Verify home page title
3.)Verify login
4.)Close  browser:one time activity

setUpClass():Executed one time before class started.
tearDownClass():Executed one time after complete of all method.

'''
from  selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMTest(unittest,TestCase):
    
    def setUpClass(cls): # first 
       cls.self.driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
        cls.self.driver.maximize_window()#Maxmize window size
        
     
    def test_homePageTitle(self,setup): # second 
        self.driver.get("https://opensource-demo.orangehrmlive.com/")   
        self.assertEqual("OrangeHRM",self.driver.title,"web page title is not matching")
        
    def test_login(self,setup): #third
        self.driver.get("https://opensource-demo.orangehrmlive.com/") 
        self.driver.find_element_by_name("txtUsername").send_keys("Admin") 
        self.driver.find_element_by_name("txtPassword").send_keys("admin123");   
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM",self.driver.title,"web page title is not matching")
    
    def tearDownClass(cls):   
        cls.driver.quit()   
        print("Test completed....")
if__name__=='__main  '         
        
        
        
        
        