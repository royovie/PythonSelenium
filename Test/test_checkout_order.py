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

    #assert items and add to cart
    #item 1
    actual = "Sauce Labs Backpack"
    expected = "Sauce Labs Backpack"
    assert actual == expected
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    time.sleep(1)
    # item 2
    actual = "Sauce Labs Bike Light"
    expected = "Sauce Labs Bike Light"
    assert actual == expected
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    time.sleep(1)
    # item 3
    actual = "Sauce Labs Bolt T-Shirt"
    expected = "Sauce Labs Bolt T-Shirt"
    assert actual == expected
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    time.sleep(1)
    # item 4
    actual = "Sauce Labs Fleece Jacket"
    expected = "Sauce Labs Fleece Jacket"
    assert actual == expected
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()
    time.sleep(1)
    # item 5
    actual = "Sauce Labs Onesie"
    expected = "Sauce Labs Onesie"
    assert actual == expected
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
    time.sleep(1)
    # item 6
    actual = "Test.allTheThings() T-Shirt (Red)"
    expected = "Test.allTheThings() T-Shirt (Red)"
    assert actual == expected
    driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()
    time.sleep(1)

    #click cart button
    driver.find_element(By.ID, 'shopping_cart_container').click()
    time.sleep(1)

    #click checkout button
    driver.find_element(By.ID, 'checkout').click()
    time.sleep(1)

    #fill your checkout Information
    #firstname
    driver.find_element(By.ID, 'first-name').send_keys('John')
    #lastname
    driver.find_element(By,ID,'last-name').send_keys('Fake')
    #postalcode
    driver.find_element(By, ID,'postal-code').send_keys('12345')
    #continue to checkout
    driver.find_element(By, ID, 'continue').click()

    #Checkout:Overview page
    actual= "Checkout: Overview"
    expected = "Checkout: Overview"
    assert actual==expected
    #Finish shopping button
    driver.find_element(By, ID, 'finish').click()

    #Checkout:Complete!
    actual = "Checkout: Complete!"
    expected = "Checkout: Complete!"
    assert actual == expected
    #order complete
    actual = "Thank you for your order!"
    expected = "Thank you for your order!"
    assert actual == expected
    #back Home button
    driver.find_element(By, ID, 'back-to-products').click()

