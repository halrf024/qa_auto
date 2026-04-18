from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com")

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def is_open(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
            return True
        except:
            return False
        
    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container.error"))
        ).text
    
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_open(self):
        # проверяем что мы на странице товаров
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
            return True
        except:
            return False

    def open_menu(self):
        # открываем бургер меню
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()

    def click_logout(self):
        # нажимаем logout
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
        ).click()

    def get_item_count(self):
        # возвращает количество товаров на странице
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        return len(items)
    
    def get_title(self):
        # возвращает текст заголовка страницы
        return self.driver.find_element(By.CLASS_NAME, "title").text
    
    def get_item_price(self, item_name):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == item_name:
                return item.find_element(By.CLASS_NAME, "inventory_item_price").text
            
    def add_first_item_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    def get_cart_badge(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        ).text
