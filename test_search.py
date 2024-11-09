import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_valid_keyword(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@name, 'search')]").send_keys("Apple")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn-light')]").click()  # Click the search button
    time.sleep(2)
    product_items = driver.find_element(By.CLASS_NAME, "product-thumb").text
    assert "Apple Cinema 30" in product_items

def test_search_blank(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@name, 'search')]").send_keys("")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn-light')]").click()  # Click the search button
    time.sleep(5)
    message = driver.find_element(By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]")
    assert message.is_displayed()

def test_search_special_character(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@name, 'search')]").send_keys("@@@@@")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn-light')]").click()  # Click the search button
    time.sleep(5)
    message = driver.find_element(By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]")
    assert message.is_displayed()