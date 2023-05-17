from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)

driver.find_element(By.ID, 'user-name').send_keys("standard_user")

# Find and enter password
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Find and click Login
driver.find_element(By.ID, 'login-button').click()
time.sleep(5)

driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
