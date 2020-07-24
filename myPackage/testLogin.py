'''
Agenda:
Run all the tests in a module/file: pytest -v -s  testLogin.py 
Run all tests(from all modules)in a path: C:\Users\Dell\PycharmProjects\selenium\myPackage\
Run specific test method from a module: pytest -v -s testLogin.py::test_loginbyfacebook  

'''
import pytest

@pytest.yield_fixture()
def setUp():  
    print("Opening URL to Login")
    yield
    print("Closing browser after Login")
    
def test_loginbyemail(setUp):
    print("This is Login by email test")
    
def test_loginbyfacebook(setUp):
    print("This is Login by email test")    