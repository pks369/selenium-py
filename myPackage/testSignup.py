import pytest

@pytest.yield_fixture()
def setUp():  
    print("Opening URL to Signup")
    yield
    print("Closing browser after Signup")
    
def test_signupbyemail(setUp):
    print("This is Signup  by email test")
    
def test_signupbyfacebook(setUp):
    print("This is Signup  by facebook  test")    