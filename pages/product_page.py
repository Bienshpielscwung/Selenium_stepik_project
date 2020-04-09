from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        basket_link.click()

    def should_be_name_product_equals_to_name_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_BASKET).text
        assert name_product == name_basket, 'Name product on page not equals name the product in basket'

    def should_be_price_product_equals_to_name_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_BASKET).text
        assert price_product == price_basket, 'Price product on page not equals price the product in basket'
