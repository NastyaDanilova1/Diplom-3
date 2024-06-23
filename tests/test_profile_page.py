from data import Url
from locators import LoginPageLocators

from pages.profile_page import ProfilePage
from conftest import *


class TestProfilePage:

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_order_history_link(self, get_browser, create_new_user_by_api, login_new_user):
        driver = login_new_user
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        profile_page.click_order_history_link()

        assert profile_page.order_history_is_active()
        assert profile_page.get_current_url() == Url.ORDER_HISTORY_URL


    @allure.title('Проверяем выход из аккаунта')
    def test_exit_account(self, get_browser, create_new_user_by_api, login_new_user):
        driver = login_new_user
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        profile_page.click_exit_button()
        profile_page.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)

        assert profile_page.get_current_url() == Url.LOGIN_PAGE_URL

