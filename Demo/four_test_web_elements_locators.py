"""
# Google search
from selenium import webdriver
import time

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.get("https://google.com")

searchbox = driver.find_element_by_name("q")
searchbox.send_keys("Automation step by step")
time.sleep(5)

button = driver.find_element_by_name("btnK")
button.click()

driver.close()
driver.quit()

print("Test Completed")
"""

# Orange HRM demo website (https://opensource-demo.orangehrmlive.com)

