'''
@author: Pappu Kumar Singh
Agenda:Work with pytest fixtures
Fixtures: Is to provide a fixed baseline upon which tests can reliably and repeatedly execute.
1.)@pytest.fixtures():Execute specific method before every test method .
2.)@pytest.yield_fixtures():Execute specific method before & After every test method.
'''
import pytest

@pytest.fixture() #decorator method
def setup():  
    print("Once before every method")
    
def testmethod1(setup):
    print("This is test method1")
    
    
def testmethod2(setup):
    print("This is test method2")
    
    