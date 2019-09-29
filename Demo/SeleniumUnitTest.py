import unittest
import HtmlTestRunner
from selenium import webdriver

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        variable = self.driver.title
        print(variable)
        self.assertEqual(variable, "Automation step by step - Google-Suche")

    def test_search_2(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Madhu Chandra")
        self.driver.find_element_by_name("btnK").click()
        variable = self.driver.title
        print(variable)
        self.assertEqual(variable, "Madhu Chandra - Google-Suche")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/madhu/PycharmProjects/Selenium/Reports'), verbosity=2)