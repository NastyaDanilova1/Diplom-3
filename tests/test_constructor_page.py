from data import Url
from pages.orders_page import OrdersPage
from conftest import *


class TestConstructorPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_open_constructor_by_link(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.open_feed_page()
        orders_page.click_constructor_link()
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_login_button()

        assert constructor_page.get_current_url() == Url.MAIN_PAGE_URL+'/'


    @allure.title('Проверяем переход по клику на «Лента заказов»')
    def test_open_orders_list_by_link(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_feed_link()

        orders_page = OrdersPage(driver)
        orders_page.wait_total_today()

        assert orders_page.feed_is_active()
        assert orders_page.get_current_url() == Url.FEED_PAGE_URL


    @allure.title('Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_modal_window(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_ingredient_link()
        constructor_page.ingredient_details_is_opened()

        assert constructor_page.details_title_is_visible()


    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_modal_window(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_ingredient_link()
        element = constructor_page.ingredient_details_is_opened()
        constructor_page.click_details_close_link()
        constructor_page.ingredient_details_is_closed()

        assert element.get_attribute('class') == MainPageLocators.DETAILS_LINK_CLASS


    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_append_ingredient_in_order_counter_more(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        counter_before = constructor_page.get_buns_counter()
        constructor_page.drag_and_drop_bun()
        counter_after = constructor_page.get_buns_counter()

        assert counter_after > counter_before


    @allure.title('Проверяем, что авторизованный пользователь может оформить заказ')
    def test_checkout_order_by_authorized_user(self, driver, create_new_user_by_api, login_new_user):
        constructor_page = ConstructorPage(driver)
        constructor_page._create_order()

        assert constructor_page.order_details_is_visible()

