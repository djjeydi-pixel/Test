from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Локаторы для страницы авторизации (https://www.saucedemo.com/)"""
    # Поля ввода
    USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    # Сообщение об ошибке (для проверок)
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

class InventoryPageLocators:
    """Локаторы для страницы товаров (inventory.html)"""
    # Заголовок страницы
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    # Список товаров и карточка товара
    INVENTORY_LIST = (By.CSS_SELECTOR, ".inventory_list")
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    # Кнопка добавления в корзину (для товара "Sauce Labs Backpack")
    ADD_TO_CART_BACKPACK = (By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-backpack']")
    # Иконка корзины и счетчик
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

class CartPageLocators:
    """Локаторы для страницы корзины (cart.html)"""
    # Заголовок и список товаров в корзине
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_LIST = (By.CSS_SELECTOR, ".cart_list")
    CART_ITEM = (By.CSS_SELECTOR, ".cart_item")
    # Кнопка оформления заказа
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

class CheckoutPageLocators:
    """Локаторы для страницы оформления заказа (checkout-step-one.html)"""
    # Поля ввода данных
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    # Кнопка продолжения
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")

class CheckoutOverviewLocators:
    """Локаторы для страницы подтверждения заказа (checkout-step-two.html)"""
    # Кнопка завершения заказа
    FINISH_BUTTON = (By.CSS_SELECTOR, "#finish")

class CheckoutCompleteLocators:
    """Локаторы для страницы успешного заказа (checkout-complete.html)"""
    # Заголовок об успешном заказе
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")