
from data import Url, Data
from locators import RecoveryPasswordPageLocators

from pages.recovery_password_page import RecoveryPasswordPage
from pages.reset_password_page import ResetPasswordPage
from conftest import *


class TestRecoveryPasswordPage:

    @allure.title('Проверяем переход на страницу восстановления пароля по гиперссылке «Восстановить пароль»')
    def test_forgot_password_button(self, get_browser):
        driver = get_browser
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.scroll_to_click_forgot_password_link()
        login_page.wait_for_load_element(RecoveryPasswordPageLocators.RECOVER_BUTTON)

        assert login_page.get_current_url() == Url.FORGOT_PASSWORD_PAGE_URL


    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_recovery_password_button(self, get_browser):
        driver = get_browser
        forgot_password_page = RecoveryPasswordPage(driver)
        forgot_password_page.open_and_execute_forgot_password_page(Data.USER_EMAIL)

        assert forgot_password_page.get_current_url() == Url.RESET_PASSWORD_PAGE_URL


    @allure.title('Проверяем что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_eye_button_click(self, get_browser):
        driver = get_browser
        forgot_password_page = RecoveryPasswordPage(driver)
        forgot_password_page.open_and_execute_forgot_password_page(Data.USER_EMAIL)
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_eye_button()

        assert reset_password_page.password_field_focused()

