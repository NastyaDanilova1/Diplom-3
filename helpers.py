import allure
import requests

import random
import string

class Api:

    SERVER_URL = 'https://stellarburgers.nomoreparties.site'
    API_CREATE_USER = '/api/auth/register'  # регистрация пользователя
    API_DELETE_USER = '/api/auth/user'  # удаление пользователя


class HelpersOnRequests:

    @staticmethod
    @allure.step('отправляем API-запрос на создание пользователя')
    def request_on_create_user(payload):
        request_url = f'{Api.SERVER_URL}{Api.API_CREATE_USER}'
        response = requests.post(f'{request_url}', json=payload)
        return response

    @staticmethod
    @allure.step('отправляем API-запрос на удаление пользователя')
    def request_on_delete_user(headers):
        request_url = f'{Api.SERVER_URL}{Api.API_DELETE_USER}'
        response = requests.delete(f'{request_url}', headers=headers)
        return response


class HelpersRegisterUser:
    @staticmethod
    @allure.step('генерация рандомной строки с буквами в нижнем регистре')
    def random_string(length):
        return (f"{''.join(random.choice(string.ascii_lowercase) for i in range(length))}")

    @staticmethod
    @allure.step('генерация данных пользователя')
    def generate_user_data():
        email = HelpersRegisterUser.random_string(10) + '@yandex.ru'
        password = HelpersRegisterUser.random_string(10)
        name = HelpersRegisterUser.random_string(10)
        user_data = {
            'email': email,
            'password': password,
            'name': name
        }
        return user_data

# api

    @staticmethod
    @allure.step('отправляем запрос на создание нового пользователя')
    def try_to_create_user(user_data):
        response = HelpersOnRequests.request_on_create_user(user_data)
        return response

    @staticmethod
    @allure.step('удаляем пользователя')
    def try_to_delete_user(auth_token):
        headers = {'Authorization': auth_token}
        response = HelpersOnRequests.request_on_delete_user(headers)
        return response

