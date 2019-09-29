"""
import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        self.driver.implicitly_wait(5)
        var_title = self.driver.title
        print(var_title)
        self.assertEqual(var_title, "Automation step by step - Google-Suche")

    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        self.driver.implicitly_wait(5)
        var_title = self.driver.title
        print(var_title)
        self.assertEqual(var_title, "Madhu Chandra Krishnappa")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    # def test_something(self):
    #     self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()

"""

import unittest
from selenium import webdriver
import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        self.driver.implicitly_wait(5)
        var_title_1 = self.driver.title
        print(var_title_1)
        self.assertEqual(var_title_1, "Automation step by step - Google-Suche")

    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Madhu Chandra")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("btnK").click()
        self.driver.implicitly_wait(5)
        var_title_2 = self.driver.title
        print(var_title_2)
        self.assertEqual(var_title_2, "Madhu Chandra - Google-Suche")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """

    def test_search_3(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Madhu Chandra Krishnappa")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("btnK").click()
        self.driver.implicitly_wait(5)
        var_title_3 = self.driver.title
        print(var_title_3)
        self.assertEqual(var_title_3, "Madhu Chandra - Google-Suche")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/madhu/PycharmProjects/Selenium/Reports'), verbosity=2)