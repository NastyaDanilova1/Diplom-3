from pages.orders_page import OrdersPage
from pages.profile_page import ProfilePage
from conftest import *


class TestFeedPage:

    @allure.title('Проверяем что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_modal_window(self, create_new_user_by_api, driver, login_new_user, create_order):
        feed_page = OrdersPage(driver)
        feed_page.open_feed_page()
        feed_page.click_order_link()

        assert feed_page.order_details_is_opened()


    @allure.title('Проверяем что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_are_in_orders_list(self, create_new_user_by_api, driver, login_new_user, create_order):
        profile_page = ProfilePage(driver)
        order = profile_page.get_order_from_order_history()
        order_page = OrdersPage(driver)
        order_list = order_page.get_order_number_list()
        assert order in order_list


    @allure.title('Проверяем что после оформления заказа его номер появляется в разделе В работе')
    def test_user_order_is_in_work(self, create_new_user_by_api, driver, login_new_user, create_order):
        new_order = create_order
        constructor_page = ConstructorPage(driver)
        constructor_page.click_feed_link()
        feed_page = OrdersPage(driver)
        orders_list_in_work = feed_page.get_order_list_in_work()

        assert new_order in orders_list_in_work


    @allure.title('Проверяем что создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_orders_total_more_counter(self, driver, create_new_user_by_api, login_new_user):
        feed_page = OrdersPage(driver)
        feed_page.open_feed_page()
        orders_before = feed_page.get_orders_total()
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order()
        feed_page.open_feed_page()
        orders_after = feed_page.get_orders_total()

        assert orders_after > orders_before


    @allure.title('Проверяем что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_orders_today_counter_more(self, driver, create_new_user_by_api, login_new_user):
        feed_page = OrdersPage(driver)
        feed_page.open_feed_page()
        orders_before = feed_page.get_orders_today()
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order()
        feed_page.open_feed_page()
        orders_after = feed_page.get_orders_today()

        assert orders_after > orders_before
