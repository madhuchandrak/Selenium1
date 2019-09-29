from POM.Locators.OHRMLocators import locators
class homepage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = locators.welcome_link_id
        self.logout_link_linktext = locators.logout_link_linktext

    def click_welcome_link(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout_link(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()