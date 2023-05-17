from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

driver=webdriver.Chrome(executable_path="C:/Users/ovbiy/OneDrive/Pictures/Documents/chromedriver.exe")
@pytest.fixture()
def setup():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    print(driver.title)

#Login with Valid user and Valid password
def testmethod1(setup):
    # Find and enter username
    driver.find_element(By.ID,'user-name').send_keys("standard_user")

    #Find and enter password
    driver.find_element(By.ID,"password").send_keys("secret_sauce")

    # Find and click Login
    driver.find_element(By.ID,'login-button').click()
    time.sleep(5)

    driver.find_element(By.ID,"react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID,"logout_sidebar_link").click()

#Login with Valid user and invalid password
def testmethod2(setup):
    # Find and enter username
    driver.find_element(By.ID,'user-name').send_keys("standard_user")

    #Find and enter password
    driver.find_element(By.ID,"password").send_keys("secret")

    # Find and click Login
    driver.find_element(By.ID,'login-button').click()
    time.sleep(5)
    actual = "Epic sadface: Username and password do not match any user in this service"
    expected ="Epic sadface: Username and password do not match any user in this service"
    assert actual ==expected

#Login with invalid user and Valid password
def testmethod3(setup):
    # Find and enter username
    driver.find_element(By.ID,'user-name').send_keys("standard")

    #Find and enter password
    driver.find_element(By.ID,"password").send_keys("secret_sauce")

    # Find and click Login
    driver.find_element(By.ID,'login-button').click()
    time.sleep(5)
    actual = "Epic sadface: Username and password do not match any user in this service"
    expected ="Epic sadface: Username and password do not match any user in this service"
    assert actual ==expected

#Login with invalid user and invalid password
def testmethod4(setup):
    # Find and enter username
    driver.find_element(By.ID,'user-name').send_keys("standard")

    #Find and enter password
    driver.find_element(By.ID,"password").send_keys("secret")

    # Find and click Login
    driver.find_element(By.ID,'login-button').click()
    time.sleep(5)
    actual = "Epic sadface: Username and password do not match any user in this service"
    expected ="Epic sadface: Username and password do not match any user in this service"
    assert actual ==expected

#Login with Locked user and Valid password
def testmethod5(setup):
    # Find and enter username
    driver.find_element(By.ID,'user-name').send_keys("locked_out_user")

    #Find and enter password
    driver.find_element(By.ID,"password").send_keys("secret_sauce")

    # Find and click Login
    driver.find_element(By.ID,'login-button').click()
    time.sleep(5)
    actual = "Epic sadface: Sorry, this user has been locked out."
    expected ="Epic sadface: Sorry, this user has been locked out."
    assert actual ==expected