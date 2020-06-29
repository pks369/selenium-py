'''
Agenda
   How to download file in firefox browser like doc,pdf:
'''
from selenium import  webdriver
fp=webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf") #Mime type
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir","D:\Downloadefiles")
fp.set_preference("browser.download.folderList",2)
fp.set_preference("pdfjs.disabled",True)


driver=webdriver.Firefox(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\geckodriver.exe',firefox_profile=fp)

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









