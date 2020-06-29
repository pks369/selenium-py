'''
Agenda
   How to download file in chrome browser like doc,pdf:
'''
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("prefs",{"download.default_directory":"C:\\Users\\Dell\\PycharmProjects\\selenium\\Downloadefiles"})

driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe',options=chrome_options)
# driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe')
# driver=webdriver.Ie(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\IEDriverServer.exe')

from  selenium.webdriver.common.by import By

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#Download text file
driver.find_element_by_id("textbox").send_keys("testing download text file doc")
driver.find_element_by_id("createTxt").click()# Generate file button
driver.find_element_by_id("link-to-download").click()# Download link

#Download pdf file
driver.find_element_by_id("pdfbox").send_keys("testing download text file pdf ")
driver.find_element_by_id("createPdf").click()# Generate file button
driver.find_element_by_id("pdf-link-to-download").click()#Download link
# driver.close()









