import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу по URL')
    def open_page(self, page_url):
        return self.driver.get(page_url)

    @allure.step('рещаем проблему с кнопкой')
    def problem_button_click(self, locator):
        element = WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable(locator))

        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('Открываем страницу по URL')
    def open_page(self, page_url):
        return self.driver.get(page_url)

    @allure.step('Ждем открытие страницы при переходе по ссылке URL')
    def wait_for_open_page(self, page_url):
        return WebDriverWait(self.driver, 20).until(
                    expected_conditions.url_to_be(page_url))

    @allure.step('Ждем загрузку элемента HTML по локатору')
    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ждем загрузку всех элементов HTML по локатору')
    def wait_for_load_all_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    @allure.step('Ждем пока текст элемента HTML по локатору будет отличаться от значения')
    def wait_for_changed_text(self, locator, text_value):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.none_of(expected_conditions.text_to_be_present_in_element(locator, text_value)))


    @allure.step('Ждем появление в DOM элемента HTML по локатору')
    def wait_for_presence_of_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(locator))

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Ждем кликабельности элемента по локатору')
    def wait_for_clickable_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ищем элемент HTML по локатору')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ищем все элементы HTML по локатору')
    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Вводим текст в поле по локатору')
    def set_value(self, locator, value):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator)).send_keys(value)

    @allure.step('Прокручиваем страницу до элемента по локатору')
    def scroll_to_element_by_locator(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Прокручиваем страницу до элемента по локатору')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Получаем значение поля по локатору')
    def get_value(self, locator):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator)).get_attribute("value")

    @allure.step('Получаем текст в поле по локатору')
    def get_text(self, locator):
        return (self.wait_for_load_element(locator)).text


    @allure.step('Ждем видимости элемента по локатору и кликаем')
    def click_element_by_locator(self, locator):
        WebDriverWait(self.driver, 100).until(expected_conditions.visibility_of_element_located(locator)).click()


    @allure.step('Ждем кликабельности элемента по локатору и кликаем')
    def click_element_by_locator_when_clickable(self, locator):
        element = WebDriverWait(self.driver, 20).until(
             expected_conditions.element_to_be_clickable(locator))
        element.click()

    @allure.step('Кликаем элемент')
    def click_element(self, element):
        element.click()

    @allure.step('Перемещаем элемент')
    def drag_and_drop(self, source, target):
        # action = ''
        # if (_browser == 'Chrome'):
        #     action = ActionChains(self.driver)
        # else:
        #     action = drag_and_drop(self.driver)
        #     action.drag_and_drop(source, target).perform()
        # action = ActionChains(self.driver)

        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    @allure.step('Проверяем, что в имени класса появляется текст')
    def wait_for_text_in_classname(self, locator, text):        # bool
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.text_to_be_present_in_element_attribute(locator, 'class', text))

    @allure.step('Проверяем что элемент становится невидимым')
    def wait_for_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.invisibility_of_element_located(locator))

