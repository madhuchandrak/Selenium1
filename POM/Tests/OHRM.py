from selenium import webdriver
import time
import unittest
import HtmlTestRunner

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
# In the [".."] two dots are used within the double quotes to represent 2 nested folders. Use 3 dots for 3 nested folders

from POM.Pages.OHRMLoginPage import loginpage
from POM.Pages.OHRMHomePage import homepage

class logintests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/madhu/PycharmProjects/Selenium/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(2)

    def test_login_validate(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        home = homepage(driver)
        home.click_welcome_link()
        home.click_logout_link()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.minimize_window()
        cls.driver.close()
        cls.driver.quit()
        print("Login and logout was successful")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/madhu/PycharmProjects/Selenium/Results'))