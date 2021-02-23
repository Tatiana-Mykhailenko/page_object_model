from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_not_be_view_basket_button()

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        assert 'basket' in current_url, "No 'basket' in URL"

    def should_not_be_view_basket_button(self):
        assert self.is_not_element_present(
            *BasePageLocators.BASKET_BUTTON), "'View basket' button is presented"

    def should_be_an_item_in_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_ITEMS), "No items in basket"

    def should_not_be_an_item_in_basket(self):
        assert not self.is_element_present(
            *BasketPageLocators.BASKET_ITEMS), "There is an item in basket"    

    def is_basket_empty(self):
        self.should_not_be_an_item_in_basket()
        assert self.is_element_present(
            *BasketPageLocators.CONTINUE_SHOPPING_LINK), "'Continue shopping' link is not presented"
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_TEXT), "'Empty basket' text is not presented"
        assert self.is_not_element_present(
            *BasketPageLocators.CHEKOUT_BUTTON), "'Checkout' button is presented"
        assert self.is_not_element_present(
            *BasketPageLocators.VOUCHER_BUTTON), "'Voucher' button is presented"

    def is_basket_not_empty(self):
        self.should_be_an_item_in_basket()
        assert self.is_not_element_present(
            *BasketPageLocators.CONTINUE_SHOPPING_LINK), "'Continue shopping' link is presented"
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_TEXT), "'Empty basket' text is presented"
        assert self.is_element_present(
            *BasketPageLocators.CHEKOUT_BUTTON), "'Checkout' button is not presented"
        assert self.is_element_present(
            *BasketPageLocators.VOUCHER_BUTTON), "'Voucher' button is not presented"
