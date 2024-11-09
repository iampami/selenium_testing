import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_product_to_Cart(driver):
    driver.get("https://demo.opencart.com/")
    driver.execute_script("window.scrollBy(0, 500);")  # Cuộn xuống 500px
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[contains(@title, 'iPhone')]").click()
    time.sleep(10)
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(@id, 'button-cart')]")
    add_to_cart_button.click()
    time.sleep(5)

    # Assert that the cart contains the product
    assert driver.page_source, "Success: You have added iPhone to your shopping cart!"

def test_add_product_zero_quantity(driver):
    driver.get("https://demo.opencart.com/")
    driver.execute_script("window.scrollBy(0, 500);")  # Cuộn xuống 500px
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[contains(@title, 'iPhone')]").click()
    time.sleep(10)
    quantity_input = (driver.find_element(By.XPATH, "//input[contains(@name, 'quantity')]"))
    quantity_input.clear()
    quantity_input.send_keys("0")
    time.sleep(2)
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    add_to_cart_button.click()
    time.sleep(6)

    # Assert that the cart contains the product
    assert driver.page_source, "Success: You have added iPhone to your shopping cart!"
 # loi van hien thi them duoc san pham khi nhap 0

def test_add_product_negative_quantity(driver):
    driver.get("https://demo.opencart.com/")
    driver.execute_script("window.scrollBy(0, 500);")  # Cuộn xuống 500px
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[contains(@title, 'iPhone')]").click()
    time.sleep(10)
    quantity_input = (driver.find_element(By.XPATH, "//input[contains(@name, 'quantity')]"))
    quantity_input.clear()
    quantity_input.send_keys("-1")
    time.sleep(2)
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    add_to_cart_button.click()
    time.sleep(6)

    # Assert that the cart contains the product
    assert driver.page_source, "Success: You have added iPhone to your shopping cart!"
 # loi van hien thi them duoc san pham khi nhap -1

def test_add_product_without_quantity(driver):
    driver.get("https://demo.opencart.com/")
    driver.execute_script("window.scrollBy(0, 500);")  # Cuộn xuống 500px
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[contains(@title, 'iPhone')]").click()
    time.sleep(10)
    quantity_input = (driver.find_element(By.XPATH, "//input[contains(@name, 'quantity')]"))
    quantity_input.clear()
    # quantity_input.send_keys("-1")
    time.sleep(2)
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    add_to_cart_button.click()
    time.sleep(6)

    # Assert that the cart contains the product
    assert driver.page_source, "Success: You have added iPhone to your shopping cart!"
# fail

def test_add_product_random_quantity(driver):
    driver.get("https://demo.opencart.com/")

    my_account_link = driver.find_element(By.NAME, "search")
    my_account_link.clear()
    my_account_link.send_keys("iphone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(5)
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    random_integer = random.randint(1, 100)
    # random_integer_str = str(random_integer)

    quantity.send_keys(str(random_integer))
    time.sleep(3)

    price = driver.find_element(By.CLASS_NAME, "price-new")
    numeric_value = float(price.text.replace("$", ""))

    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)
    total_value_element = driver.find_element(By.XPATH, "//td[.='Total']/following-sibling::td")
    total_value = total_value_element.text

    # Lấy giá trị số từ chuỗi actual_value và làm tròn
    total = random_integer*numeric_value
    formatted_value = f"${total:,.2f}"

    assert total_value == formatted_value, f"Expected {formatted_value} but got {total_value}"

def test_remove_to_Cart(driver):
    driver.get("https://demo.opencart.com/")
    driver.execute_script("window.scrollBy(0, 500);")  # Cuộn xuống 500px
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[contains(@title, 'iPhone')]").click()
    time.sleep(10)
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    add_to_cart_button.click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//a[contains(@href, 'route=checkout/checkout')]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//button[contains(@formaction, 'route=checkout/cart.remove')]").click()
    time.sleep(6)

    empty_cart = driver.find_element(By.XPATH, "//p[contains(text(), 'Your shopping cart is empty!')]")
    # Assert that the cart contains the product
    assert empty_cart.is_displayed()

def test_update_quantity(driver):
    driver.get("https://demo.opencart.com/")
    driver.execute_script("window.scrollBy(0, 500);")  # Cuộn xuống 500px
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[contains(@title, 'iPhone')]").click()
    time.sleep(10)
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]")
    add_to_cart_button.click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//a[contains(@href, 'route=checkout/checkout')]").click()
    time.sleep(10)
    quantity = driver.find_element(By.XPATH, "//input[contains(@name, 'quantity')]")
    quantity.clear()
    quantity.send_keys("2")
    driver.find_element(By.XPATH, "//button[contains(@formaction, 'route=checkout/cart.edit')]").click()
    time.sleep(6)

    assert driver.page_source, " Success: You have modified your shopping cart!"