"""
# Locators in individual files
class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_link_id = "welcome" # object name = welcome, object name type = link, locator type = id property
        self.logout_link_linkText = "Logout" # object name = logout, object name type = link, locator type = link text property

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()
"""
# Locators in one file
from PageObjectModel.Locators.Locators import Locators
class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()