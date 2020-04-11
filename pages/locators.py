from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "[value='Register']")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) div.alertinner strong")
    PRICE_PRODUCT_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasketPageLocators():
    BUTTON_BASKET_FROM_HEADER_PAGE = (By.CSS_SELECTOR, "span.btn-group a.btn")
    MESSAGE_OF_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
