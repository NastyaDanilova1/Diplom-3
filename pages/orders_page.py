import allure

from data import Url
from locators import OrdersPageLocators
from pages.base_page import BasePage



class OrdersPage(BasePage):

    @allure.step('Ожидаем появление числа заказов за сегодня ')
    def wait_total_today(self):
        self.wait_for_load_element(OrdersPageLocators.TOTAL_TODAY)
    @allure.step('Открываем Ленту заказов')
    def open_feed_page(self):
        self.open_page(Url.FEED_PAGE_URL)
        self.wait_total_today()

    @allure.step('кликаем ссылку "Конструктор"')
    def click_constructor_link(self):
        self.click_element_by_locator(OrdersPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Проверяем, что Лента заказов становится активным')
    def feed_is_active(self):
        return self.wait_for_text_in_classname(OrdersPageLocators.FEED_LINK,
                                               OrdersPageLocators.ACTIVE_TEXT)

    @allure.step('кликаем на 1-й заказ')
    def click_order_link(self):
        self.click_element_by_locator(OrdersPageLocators.ORDER_LINK)

    @allure.step('Проверяем, что открывается модальное окно с деталями заказа')
    def order_details_is_opened(self):
        return self.wait_for_load_element(OrdersPageLocators.ORDER_DETAILS_OPENED)

    @allure.step('Получаем список элементов страницы с номерами заказов из раздела Лента заказов')
    def __get_order_number_list_elements(self):
        return self.wait_for_load_all_elements(OrdersPageLocators.ORDER_LIST_ORDER_NUMBER)

    @allure.step('Получаем список номеров заказов в Ленте заказов')
    def get_order_number_list(self):
        self.open_feed_page()
        elements = self.__get_order_number_list_elements()
        order_list = []
        for item in elements:
            number = item.text
            order_list.append(number)
        return order_list

    @allure.step('Получаем список элементов страницы с номерами заказов в разделе "В работе"')
    def __get_order_list_in_work(self):
        return self.wait_for_load_all_elements(OrdersPageLocators.ORDER_STATUS_BOX_LIST2_ITEM_DIGIT)

    @allure.step('Получаем список номеров заказов в разделе "В работе"')
    def get_order_list_in_work(self):
        elements = self.__get_order_list_in_work()
        orders_list = []
        for element in elements:
            number = str(int(element.text))
            orders_list.append(number)
        return orders_list

    @allure.step('Получаем список элементов страницы со счетчиками "Выполнено за всё время" и "Выполнено за сегодня"')
    def __get_orders_total(self):
        return self.wait_for_load_all_elements(OrdersPageLocators.ORDER_FEED_NUMBER)

    @allure.step('Получаем счетчик "Выполнено за всё время"')
    def get_orders_total(self):
        elements = self.__get_orders_total()
        return int(str(elements[0].text))

    @allure.step('Получаем счетчик "Выполнено сегодня"')
    def get_orders_today(self):
        elements = self.__get_orders_total()
        return int(str(elements[1].text))



