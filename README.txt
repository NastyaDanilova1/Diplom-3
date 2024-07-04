Diplom3
тесты для проверки веб-приложения Stellary Burgers


Структура проекта:
- allure results - результаты тестов
- pages(base_page, constructor_page, login_page, orders_page,
profile_page, recovery_password_page, reset_password_page) - классы страниц
- tests (test_constructor_page, test_orders, test_password_recovery_page, test_profile_page) - папка с тестами
- conftest - фикстуры проекта
- data - Url,Data,Keys
- helpers - вспомогательные функции
- locators - локаторы

Генерация отчета:
$ allure serve allure_results

Генерация файла внешних зависимостей requirements.txt:
$ pip freeze > requirements.txt

