import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import InventoryPage, LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_item_count(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_item_count() == 6

def test_title(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_title() == "Products"

# rther
def test_backpack_price(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_item_price("Sauce Labs Backpack") == "$29.99"

 # grrgr
def test_wrong_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user", "wrong_password")
    
    error = login_page.get_error_message()
    assert error == "Epic sadface: Username and password do not match any user in this service"

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()

    badge = inventory_page.get_cart_badge()
    assert badge == "1"

