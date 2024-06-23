from selenium.webdriver.common.by import By


class MainPageLocators:
    # локаторы главной страницы
    ANY_BUTTON = (By.XPATH, ".//button")  # сслыка/кнопка "Оформить заказ"/"Войти в аккаунт" на Главной странице
    PROFILE_LINK = (By.XPATH, ".//a[@href='/account']")  # ссылка/кнопка Личный кабинет
    CONSTRUCTOR_LINK = (By.XPATH, ".//a[@href='/']")  # ссылк/кнопка на Конструктор
    FEED_LINK = (By.XPATH, ".//a[@href='/feed']")  # ссылка/кнопка на Ленту заказов
    ACTIVE_TEXT = 'link_active'  # текст в классе активной вкладки
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на Главной странице
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на Главной странице
    TOTAL_TODAY = (By.XPATH, ".//p[text()='Выполнено за сегодня:']")  # выполнено за сегодня заказов


    # локаторы страницы Конструктор:
    DETAILS_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]') # окно детали ингредиента
    DETAILS_TITLE_LINK = (By.XPATH, ".//h2[text()='Детали ингредиента']")  # детали ингредиента
    DETAILS_CLOSE_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]//button')
    DETAILS_LINK_CLASS = 'Modal_modal__P3_V5'
    DRAGNDROP_BUN_TARGET = (By.XPATH, './/span[text()="Перетяните булочку сюда (верх)"]') # поле для перетаскивания ингредиентов
    INGREDIENT_COUNTER_LINK = (
    By.XPATH, '//*[contains(@href,"/ingredient/")]//p[contains(@class,"counter_counter__num")]')  # счетчик ингредиента
    INGREDIENT_LINK = (By.XPATH, '//*[contains(@href,"/ingredient/")]')  # ингредиент булка
    INGREDIENT_3_LINK = (By.XPATH, '(//*[contains(@href,"/ingredient/")])[3]')  # ингредиент соус
    INGREDIENT_7_LINK = (By.XPATH, '(//*[contains(@href,"/ingredient/")])[7]')  # ингредиент начинка
    DRAGNDROP_BURGER_TARGET = (By.XPATH, '//*[contains(@class,"BurgerConstructor_basket__list")]')

    # модальное окно - заказ оформлен
    ORDER_MODAL_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened__3ISw4")]')
    ORDER_CLOSE_BUTTON = (By.XPATH, './/button[contains(@class,"Modal_modal__close")]') # кнопка закрытия
    ORDER_MODAL_ORDER_NUMBER = (By.XPATH, './/h2[contains(@class,"Modal_modal__title_shadow")]')  # номер нового заказа


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")  # поле для ввода email
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']") # поле для ввода пароля
    FORGOT_PAGE_LINK = (
    By.XPATH, ".//a[text()='Восстановить пароль']")  # cсылка/кнопка "Восстановить пароль" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # сслыка/кнопка "Войти"

class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[@href='/account/order-history']")  # ссылка/кнопка "История заказов"
    ORDER_HISTORY_IS_ACTIVE = 'Account_link_active'  # история заказов активна
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # ссылка/кнопка "Выход"
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")  # ссылка/кнопка "Сохранить"
    ORDER_HISTORY_ORDER_NUMBER = (By.XPATH,

                                  './/li[contains(@class,"OrderHistory_listItem")]/a/div/p[contains(@class,"digits")]')
class OrdersPageLocators:
    ORDER_LIST_ORDER_NUMBER = (By.XPATH, './/p[contains(@class,"text_type_digits-default")]')  # номер нового заказа
    ORDER_LINK = (By.XPATH, '//*[contains(@href,"/feed/")]')
    ORDER_DETAILS_OPENED = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]') # модальное окно с деталями заказа
    ORDER_STATUS_BOX_LIST2_ITEM_DIGIT \
        = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[2]/li[contains(@class,"digits")]')
    ORDER_FEED_NUMBER = (By.XPATH, './/p[contains(@class,"OrderFeed_number")]')


class RecoveryPasswordPageLocators:
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")  # сслыка/кнопка "Восстановить"
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")  # поле для ввода email


class ResetPasswordPageLocators:
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")  # Кнопка "Сохранить"
    EYE_ICON = (By.XPATH, '//*[contains(@class,"input__icon")]')
    PASSWORD_PLACEHOLDER = (By.XPATH, ".//label[text()='Пароль']")  # плейсхолдер поля "Пароль"
    FOCUSED_FIELD = (By.XPATH, '//*[contains(@class,"input__placeholder")]')  # класс поля "Пароль"
    FOCUSED_TEXT = 'input__placeholder-focused'

