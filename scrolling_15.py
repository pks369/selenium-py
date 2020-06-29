'''
Agenda
   Scrolling
  1.)Scroll down page by pixel.
  2.)Scroll down page till the element is visible.
  3.)Scroll down page till end.

'''
from selenium import  webdriver
from  selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')
# driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()#Maxmize window size
driver.execute_script("window.scrollBy(0,2000)"," ")  # Scroll down page by pixel

flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();", flag) #Scroll down page till the element is visible
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #Scroll down page till end.

