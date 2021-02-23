from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "'Add to basket' button is not presented"
    
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_info(self):
        title = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE).text
        price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        return title, price

    def get_product_info_from_messages(self):
        title = self.browser.find_element(
            *ProductPageLocators.BASKET_INFO_MESSAGE_PRODUCT_TITLE).text
        price = self.browser.find_element(
            *ProductPageLocators.BASKET_INFO_MESSAGE_TOTAL_PRICE).text
        return title, price

    def should_be_messages_after_adding(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_INFO_MESSAGE_WITH_PRODUCT_INFO), "Message with added product is not presented"
        assert self.is_element_present(
            *ProductPageLocators.BASKET_INFO_MESSAGE_WITH_PRICE_INFO), "Message with added price is not presented"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should disappear"
