import allure
import pytest
from selenium import webdriver

from data import RESPONSE_KEYS
from helpers import HelpersRegisterUser
from locators import MainPageLocators
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


# работа с WebDriver

@allure.title('Открываем окно веб-браузера')
@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        driver = webdriver.Chrome()
    elif 'firefox' in request.param:
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title('Входим под новым пользователем на сайт')
@pytest.fixture
def login_new_user(driver, create_new_user_by_api):
    user_data = create_new_user_by_api
    email = user_data['email']
    password = user_data['password']
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_user_data(email, password)
    login_page.click_login_button()
    login_page.wait_for_load_element(MainPageLocators.ORDER_BUTTON)


@allure.title('Создаем заказ для авторизованного пользователя')
@pytest.fixture
def create_order(driver, create_new_user_by_api, login_new_user):
    constructor_page = ConstructorPage(driver)
    order = constructor_page.create_order()
    return order


#
# Функции для работы с API
#
@allure.title('Создаем нового пользователя с помощью API')
@pytest.fixture
def create_new_user_by_api():
    user_data = HelpersRegisterUser.generate_user_data()
    response = HelpersRegisterUser.try_to_create_user(user_data)
    received_body = response.json()
    auth_token = received_body[RESPONSE_KEYS.ACCESS_TOKEN]
    yield user_data

    HelpersRegisterUser.try_to_delete_user(auth_token)

