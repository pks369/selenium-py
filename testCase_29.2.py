import  unittest
from  selenium  import  webdriver
class searchEngineTest(unittest.TestCase):
    def testGoogle(self):
        self.driver=webdriver.Chrome(executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe)
        self.driver("https://www.google.com/")
        print("Title of the page is:" ,+self.driver.title)
        self.driver.close()

    def testBing(self):
            self.driver = webdriver.Chrome(
                executable_path='C:\\Users\\Dell\\PycharmProjects\\selenium\\drivers\\chromedriver.exe)
            self.driver("https://www.bing.com/")
            print("Title of the page is:", + self.driver.title)
            self.driver.close()

if __name__ == " __main__ ":
    unittest.main()

