import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from test_login import test_valid_login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_submission_with_login(driver):
    test_valid_login(driver)
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@href , 'route=common/home')]").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")  # Cuộn xuống 700px
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Us')]").click()
    time.sleep(10)
    # driver.find_element(By.XPATH, "//input[contains(@name, 'name')]").send_keys("Candy")
    # driver.find_element(By.XPATH, "//input[contains(@name, 'email')]").send_keys("jcandie@gmail.com")
    driver.find_element(By.XPATH, "//textarea[contains(@name, 'enquiry')]").send_keys("hahahahahahahahahahaha")
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
    time.sleep(2)

    account_header = driver.find_element(By.XPATH, "//p[normalize-space()='Your enquiry has been successfully sent to the store owner!']")
    assert account_header.is_displayed()

def test_form_submission_without_login(driver):
    driver.get("https://demo.opencart.com/")
    driver.execute_script("window.scrollBy(0, 700);")  # Cuộn xuống 700px
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Us')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[contains(@name, 'name')]").send_keys("Candy")
    driver.find_element(By.XPATH, "//input[contains(@name, 'email')]").send_keys("jcandie@gmail.com")
    driver.find_element(By.XPATH, "//textarea[contains(@name, 'enquiry')]").send_keys("hahahahahahahahahahaha")
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
    time.sleep(2)

    account_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Contact Us']")
    assert account_header.is_displayed()

def test_form_submission_under_10_character(driver):
    driver.get("https://demo.opencart.com/")
    driver.execute_script("window.scrollBy(0, 700);")  # Cuộn xuống 700px
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Us')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[contains(@name, 'name')]").send_keys("Candy")
    driver.find_element(By.XPATH, "//input[contains(@name, 'email')]").send_keys("jcandie@gmail.com")
    driver.find_element(By.XPATH, "//textarea[contains(@name, 'enquiry')]").send_keys("haha")
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 700);")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
    time.sleep(2)

    account_header = driver.find_element(By.XPATH, "//div[@id='error-enquiry']")
    assert account_header.is_displayed()
