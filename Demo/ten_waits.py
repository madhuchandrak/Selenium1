"""
# Implicit wait
from selenium import webdriver

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10) # Implicit wait

driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Madhu Chandra")
driver.find_element_by_name("btnK").click()

driver.minimize_window()
driver.close()
driver.quit()
print("Done")
"""

# Explicit wait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Madhu Chandra")

wait = WebDriverWait(driver, 10)
try:
    element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
    print("Element is clickable")
except:
    print("Element is not clickable")
    exit(1)
element.click()

driver.minimize_window()
driver.close()
driver.quit()
print("Done")