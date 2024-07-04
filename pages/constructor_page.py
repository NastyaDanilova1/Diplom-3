import allure

from data import Url
from locators import *
from pages.base_page import BasePage
from selenium.webdriver import ActionChains

class ConstructorPage(BasePage):

    @allure.step('Ожидаем появление кнопки')
    def wait_login_button(self):
        self.wait_for_load_element(MainPageLocators.LOGIN_BUTTON)
    @allure.step('Открываем Главную страницу по url')
    def open_constructor_page(self):
        self.open_page(Url.MAIN_PAGE_URL)
        self.wait_for_load_element(MainPageLocators.ANY_BUTTON)

    @allure.step('Кликаем ссылку "Лента заказов"')
    def click_feed_link(self):
        self.click_element_by_locator(MainPageLocators.FEED_LINK)

    @allure.step('Кликаем ссылку "Личный кабинет"')
    def click_profile_link(self):
        self.click_element_by_locator(MainPageLocators.PROFILE_LINK)

    @allure.step('Открываем Личный кабинет по ссылке на Главной странице')
    def open_profile_page_by_link(self):
        self.open_constructor_page()
        self.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
        self.click_profile_link()
        self.wait_for_load_element(ProfilePageLocators.SAVE_BUTTON)

    @allure.step('Кликаем на 1-й ингредиент')
    def click_ingredient_link(self):
        self.click_element_by_locator(MainPageLocators.INGREDIENT_LINK)

    @allure.step('Проверяем, что открывается карточка деталей')
    def ingredient_details_is_opened(self):
        return self.wait_for_load_element(MainPageLocators.DETAILS_OPENED_LINK)

    @allure.step('Проверяем, что появился заголовок Детали ингредиента')
    def details_title_is_visible(self):
        return self.wait_for_load_element(MainPageLocators.DETAILS_TITLE_LINK)

    @allure.step('Кликаем на крестик')
    def click_details_close_link(self):
        self.click_element_by_locator(MainPageLocators.DETAILS_CLOSE_LINK)

    @allure.step('Кликаем на крестик')
    def click_details_close_link(self):
        self.click_element_by_locator(MainPageLocators.DETAILS_CLOSE_LINK)

    @allure.step('Проверяем что заголовок Детали ингредиента скрыт')
    def ingredient_details_is_closed(self):
        self.wait_for_invisibility_of_element(MainPageLocators.DETAILS_TITLE_LINK)

    @allure.step('Добавляем булку в заказ')
    def drag_and_drop_bun(self):
        action = ActionChains(self.driver)
        source = self.wait_for_load_element(MainPageLocators.INGREDIENT_LINK)
        target = self.wait_for_load_element(MainPageLocators.DRAGNDROP_BUN_TARGET)
        action.drag_and_drop(source, target).perform()

    @allure.step('Получаем счетчик булок')
    def get_buns_counter(self):
        counter = self.get_text(MainPageLocators.INGREDIENT_COUNTER_LINK)
        return int(counter)

    @allure.step('Прокручиваем страницу к соусу')
    def scroll_to_sauce(self):
        return self.scroll_to_element_by_locator(MainPageLocators.INGREDIENT_3_LINK)


    @allure.step('Прокручиваем страницу к начинке')
    def scroll_to_filling(self):
        return  self.scroll_to_element_by_locator(MainPageLocators.INGREDIENT_7_LINK)

    @allure.step('Добавляем соус в заказ')
    def drag_and_drop_sauce(self):
        self.scroll_to_sauce()
        source = self.wait_for_load_element(MainPageLocators.INGREDIENT_3_LINK)
        target = self.wait_for_load_element(MainPageLocators.DRAGNDROP_BURGER_TARGET)
        self.drag_and_drop(source, target)


    @allure.step('Добавляем начинку в заказ')
    def drag_and_drop_filling(self):
        self.scroll_to_filling()
        source = self.wait_for_load_element(MainPageLocators.INGREDIENT_7_LINK)
        target = self.wait_for_load_element(MainPageLocators.DRAGNDROP_BURGER_TARGET)
        self.drag_and_drop(source, target)

    @allure.step('Кликаем кнопку Оформить заказ')
    def click_order_button(self):
        self.click_element_by_locator(MainPageLocators.ORDER_BUTTON)

    @allure.step('Ждем, что появилось всплывающее окно с деталями заказа')
    def order_details_is_visible(self):
        return self.wait_for_load_element(MainPageLocators.ORDER_MODAL_OPENED_LINK)

    @allure.step('Получаем номер заказа')
    def get_new_order_number(self):
        return self.wait_for_load_element(MainPageLocators.ORDER_MODAL_ORDER_NUMBER).text

    @allure.step('Формируем заказ и кликаем кнопку "Оформить заказ"')
    def _create_order(self):
        self.open_constructor_page()
        self.drag_and_drop_bun()
        self.drag_and_drop_sauce()
        self.drag_and_drop_filling()
        self.click_order_button()

    @allure.step('Создаем заказ и получаем его номер')
    def create_order(self):
        self._create_order()
        self.order_details_is_visible()
        self.wait_for_changed_text(MainPageLocators.ORDER_MODAL_ORDER_NUMBER, '9999')
        order = self.get_new_order_number()
        self.click_element_by_locator(MainPageLocators.ORDER_CLOSE_BUTTON)
        return str(order)
