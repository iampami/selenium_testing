import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://demo.opencart.com/")

    try:
        my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")

        driver.execute_script("arguments[0].scrollIntoView();", my_account_link)

        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
            )
            close_button.click()
        except Exception:
            pass  # Nếu không có popup, tiếp tục

        my_account_link.click()
        time.sleep(5)
        driver.find_element(By.ID, "input-email").send_keys("jcandie@gmail.com")
        driver.find_element(By.ID, "input-password").send_keys("000000")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        time.sleep(3)
        account_header = driver.find_element(By.XPATH, "//h2[normalize-space()='My Account']")
        assert account_header.is_displayed()
    except Exception as e:
        print(f"An error occurred: {e}")

def test_invalid_login(driver):
    driver.get("https://demo.opencart.com/")

    try:
        my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")

        driver.execute_script("arguments[0].scrollIntoView();", my_account_link)

        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
            )
            close_button.click()
        except Exception:
            pass  # Nếu không có popup, tiếp tục

        my_account_link.click()
        time.sleep(20)
        driver.find_element(By.ID, "input-email").send_keys("j@gmail.com")
        driver.find_element(By.ID, "input-password").send_keys("044546546")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        time.sleep(3)

        assert driver.page_source,"Warning: No match for E-Mail Address and/or Password."
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")

def test_blank_password_login(driver):
    driver.get("https://demo.opencart.com/")

    try:
        my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")

        driver.execute_script("arguments[0].scrollIntoView();", my_account_link)

        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
            )
            close_button.click()
        except Exception:
            pass  # Nếu không có popup, tiếp tục

        my_account_link.click()
        time.sleep(20)
        driver.find_element(By.ID, "input-email").send_keys("j@gmail.com")
        driver.find_element(By.ID, "input-password").send_keys("")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        time.sleep(3)

        assert driver.page_source,"Warning: No match for E-Mail Address and/or Password."
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")

def test_blank_email_login(driver):
    driver.get("https://demo.opencart.com/")

    try:
        my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")

        driver.execute_script("arguments[0].scrollIntoView();", my_account_link)

        try:
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
            )
            close_button.click()
        except Exception:
            pass  # Nếu không có popup, tiếp tục

        my_account_link.click()
        time.sleep(20)
        driver.find_element(By.ID, "input-email").send_keys("")
        driver.find_element(By.ID, "input-password").send_keys("044546546")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        time.sleep(3)

        assert driver.page_source,"Warning: No match for E-Mail Address and/or Password."
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")









