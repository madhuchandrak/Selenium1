import unittest
from selenium import webdriver
# import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_home(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.implicitly_wait(3)
        home_page = self.driver.title
        print(home_page)
        self.assertEqual(home_page, "OrangeHRM")

    def test_login(self):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        signin_page = self.driver.title
        print(signin_page)
        self.assertEqual(signin_page, "OrangeHRM")
        self.driver.implicitly_wait(5)

    # def test_admin_page(self):
    #     self.driver.find_element_by_css_selector("#menu_admin_viewAdminModule > b > font > font").click()
    #     self.driver.implicitly_wait(5)
    #     print(self.driver.title)
    #
    # def test_add_user(self):
    #     self.driver.find_element_by_id("btnAdd").click()
    #     print(self.driver.title)
    #     self.driver.find_element_by_id("systemUser_employeeName_empName").send_keys("Russel Hamilton")
    #     self.driver.find_element_by_id("systemUser_userName").send_keys("Berlin_6")
    #     self.driver.find_element_by_id("systemUser_password").send_keys("Berlin@123")
    #     self.driver.find_element_by_id("systemUser_confirmPassword").send_keys("Berlin@123")
    #     self.driver.find_element_by_id("btnSave").click()
    #     print(self.driver.title)
    #     self.driver.implicitly_wait(5)
    #
    # def test_dashboard(self):
    #     self.driver.find_element_by_css_selector("#menu_dashboard_index > b").click()
    #     self.driver.implicitly_wait(5)

    def test_logout(self):
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_css_selector("#welcome-menu > ul > li:nth-child(2) > a").click()
        self.driver.implicitly_wait(5)
        logout_page = self.driver.title
        print(logout_page)
        self.assertEqual(logout_page, "OrangeHRM")
        self.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("User added successfully")

    if __name__ == '__main__':
        unittest.main()

        # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/madhu/PycharmProjects/Selenium/Reports'), verbosity=2)