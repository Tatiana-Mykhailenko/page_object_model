from selenium.webdriver.common.by import By

class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span>a[href*='basket']")
    BREADCRUMB_ACTIVE = (By.CSS_SELECTOR, ".breadcrumb .active")
    PAGE_HEADER = (By.CSS_SELECTOR, ".page-header .action")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD=(By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (
        By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class MainPageLocators():
    
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():

    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, "#messages>div:first-child")
    BASKET_INFO_MESSAGE_WITH_PRODUCT_INFO = (
        By.CSS_SELECTOR, "#messages>div:first-child")
    BASKET_INFO_MESSAGE_PRODUCT_TITLE = (
        By.CSS_SELECTOR, "#messages>div:first-child>div>strong")
    BASKET_INFO_MESSAGE_WITH_PRICE_INFO=(By.CLASS_NAME, "alert-info")
    BASKET_INFO_MESSAGE_TOTAL_PRICE = (
        By.CSS_SELECTOR, "#messages>div>div>p>strong")
    
class BasketPageLocators():
    CHEKOUT_BUTTON = (By.CSS_SELECTOR, "a[href *= 'checkout']")
    VOUCHER_BUTTON = (By.CSS_SELECTOR, "a[href *= 'voucher']")
    BASKET_IS_EMPTY_TEXT =  (By.CSS_SELECTOR, "#content_inner>p")
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner>p>a[href]")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
