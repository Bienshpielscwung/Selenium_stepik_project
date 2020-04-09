from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    NAME_PRODUCT_BASKET = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) div.alertinner strong")
    PRICE_PRODUCT_BASKET = (By.CSS_SELECTOR, "div.alertinner p strong")