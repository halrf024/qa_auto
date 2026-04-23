# QA Automation Tests

Учебный проект по автоматизации тестирования. Тесты написаны для сайта [saucedemo.com](https://www.saucedemo.com).

## Технологии

- Python 3.11
- Selenium
- pytest
- Page Object Model

## Структура проекта

tests/
├── pages.py        # Page Objects (LoginPage, InventoryPage, CartPage, CheckoutPage)
└── test_login.py   # Тесты

## Тесты

- `test_item_count` — проверка количества товаров на странице
- `test_title` — проверка заголовка страницы
- `test_backpack_price` — проверка цены товара
- `test_wrong_login` — негативный логин
- `test_add_to_cart` — добавление товара в корзину
- `test_url_after_login` — проверка URL после логина
- `test_cart_count` — количество товаров в корзине
- `test_checkout` — оформление заказа (E2E: логин → корзина → checkout → оплата)

## Запуск

```bash
py -m pytest -v
```
