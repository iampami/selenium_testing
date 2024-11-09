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

def test_navigation(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(10)
    driver.find_element(By.LINK_TEXT, "Desktops").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "PC (0)").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Laptops & Notebooks (5)").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Components (2)").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Monitors (2)").click()
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(5)
    product_items = driver.find_element(By.CLASS_NAME, "product-thumb").text

    assert "Apple Cinema 30" in product_items