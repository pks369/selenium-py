'''
Agenda:
1.)pipenv install  pytest-html

2.)Execute:multiple task  step by step based on requirments.

3.)pytest -v -s --html=report.html --self-contained-html  testOrangeHRM_44.py

4.)yield is generator keyword.

'''

from selenium import webdriver

import  pytest

class TestOrangeHRM(): 
   
    @pytest.fixture() #run before any test 1
    
    def setup(self):
        global driver
        self.driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
        self.driver.maximize_window()#Maxmize window size
        
        yield  #generator run after any test 3
        self.driver.close()

    def test_homePageTitle(self,setup): #run after any test 2
        self.driver.get("https://opensource-demo.orangehrmlive.com/")   
        assert self.driver.title=="OrangeHRM"
        
    def test_login(self,setup): #run after any test 4
        self.driver.get("https://opensource-demo.orangehrmlive.com/") 
        self.driver.find_element_by_id("txtUsername").send_keys("Admin") 
        self.driver.find_element_by_id("txtPassword").send_keys("admin123");   
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title=="OrangeHRM"
        
        
        