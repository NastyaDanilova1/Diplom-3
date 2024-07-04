import allure

from data import *
from locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):

    @allure.step('Открываем страницу восстановления пароля')
    def open_forgot_password_page(self):
        return self.open_page(Url.FORGOT_PASSWORD_PAGE_URL)

    @allure.step('Ждем загрузку и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_email_field(self):
        self.wait_for_load_element(RecoveryPasswordPageLocators.EMAIL_FIELD)
        self.scroll_to_element_by_locator(RecoveryPasswordPageLocators.RECOVER_BUTTON)
        self.click_element_by_locator_when_clickable(RecoveryPasswordPageLocators.EMAIL_FIELD)

    @allure.step('Открываем страницу восстановления пароля, вводим почту и кликаем кнопку "Восстановить"')
    def open_and_execute_forgot_password_page(self, email):
        self.open_forgot_password_page()
        self.wait_for_load_element(RecoveryPasswordPageLocators.RECOVER_BUTTON)
        self.scroll_to_click_email_field()
        self.set_value(RecoveryPasswordPageLocators.EMAIL_FIELD, email)
        self.click_element_by_locator_when_clickable(RecoveryPasswordPageLocators.RECOVER_BUTTON)
        self.wait_for_load_element(RecoveryPasswordPageLocators.SAVE_BUTTON)

