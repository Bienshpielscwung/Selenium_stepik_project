from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_OF_EMPTY_BASKET), \
            "Basket is not empty, but should be"

    def should_not_product_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Product is presented in basket, but should not be"
