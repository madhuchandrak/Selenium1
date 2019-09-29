"""
# method number 1

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options, executable_path="../drivers/chromedriver.exe")

driver.get("https://google.com")
print(driver.title)

driver.close()
driver.quit()

print("Test Completed")

"""

"""

# method number 2

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options, executable_path="../drivers/chromedriver.exe")

driver.get("https://google.com")
print(driver.title)

driver.close()
driver.quit()

print("Test Completed")

"""

"""
# method number 2 (extended)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable=extensions")

driver = webdriver.Chrome(options=chrome_options, executable_path="../drivers/chromedriver.exe")

driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
print(driver.title)

driver.close()
driver.quit()

print("Test Completed")

"""

"""

from selenium import webdriver

chrome_headless = webdriver.ChromeOptions()
chrome_headless.add_argument("--headless")

driver = webdriver.Chrome(options =chrome_headless, executable_path="../drivers/chromedriver.exe")

driver.get("https://www.google.com")
print(driver.title)
driver.close()
driver.quit()
print("Test Completed Successfully")

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_headless = Options()
chrome_headless.add_argument("--headless")
chrome_headless.add_argument("--disable=extensions")

driver = webdriver.Chrome(options =chrome_headless, executable_path="../drivers/chromedriver.exe")

driver.get("https://www.google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()
print("Test Completed Successfully")