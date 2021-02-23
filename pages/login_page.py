from .base_page import BasePage
from .locators import LoginPageLocators
#import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, "No 'login' in URL"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"
        
    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_EMAIL), "Register email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD), "Register password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_PASSWORD_CONFIRM), "Register confirm password is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"
        
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL)
        password_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD)
        confirm_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        submit_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_field.send_keys(password)
        submit_button.click()
