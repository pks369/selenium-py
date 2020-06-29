'''
Agenda
   Cookies:

'''
from selenium import  webdriver
driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

driver.get("https://www.amazon.in/")
driver.maximize_window()#Maxmize window size
#Capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))

#Adding new cookies to the browser
cookies={'name':'Mycookie','value':'1234567890'}
cookies=driver.get_cookies()
print(len(cookies))# no of  cookies after  adding new cookie
print(cookies)# print  all  the pair cookies


#Deleting  cookie
driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print(len(cookies))# print no of cookie after the cookie
















