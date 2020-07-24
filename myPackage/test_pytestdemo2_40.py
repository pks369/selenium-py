'''
@author: Pappu Kumar Singh
Agenda:Work with pytest fixtures
'''
import pytest
@pytest.fixture()
def setup(): 
    print("Once before every method")
    yield 
    print("Once before every method")
    
def testmethod1(setup):
    print("This is test method1")
        
def testmethod2(setup):
    print("This is test method2")
    
    