"""
# Locators in individual files
class LoginPage():

    def __init__(self, driver): # this is a constructor
        self.driver = driver

        # below mentioned are the locators of the login page
        self.username_textbox_id = "txtUsername" # object name = username, object name type = textbox, locator type = id
        self.password_textbox_id = "txtPassword" # object name = password, object name type = textbox, locator type = id
        self.login_button_id = "btnLogin"  # object name = button, object name type = button, locator type = id

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
"""
# Locators in one file
from PageObjectModel.Locators.Locators import Locators
class LoginPage():

    def __init__(self, driver): # this is a constructor
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()