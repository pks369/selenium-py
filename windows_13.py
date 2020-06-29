'''
Agenda
Work wih browser windows: Switch one browser to another close & quit.
  1.)driver.current_window_handle : Parent windows browser.
  2.)driver.window_handles: All browser.
'''

from selenium import  webdriver
from  selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe')
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')

driver.get('http://demo.automationtesting.in/Windows.html')
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)# CDwindow-956C2AC6A9FABD50DB2742B5B522CAD6 parents  windows
handles=driver.window_handles # returns all the values of opened  browser window
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=='Frames & windows':
        driver.close() # close only parent browser
    driver.quit()
    driver.quit()










