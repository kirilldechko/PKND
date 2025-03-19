from time import sleep

import dotenv
import os
import allure

from pages.authorisation_page.auth_page_data import authorisation_page_data as auth_p_data

# Загружаем переменные окружения из файла .env
dotenv.load_dotenv()

# Получаем значения переменных окружения
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# Тестовые данные на странице авторизации
authorisation_data = {
    "page_name": auth_p_data.page_name,
    "enter_button_name": auth_p_data.enter_button_name,
    "check_box_fild_name": auth_p_data.check_box_fild_name,
    "login_placeholder": auth_p_data.login_placeholder,
    "password_placeholder": auth_p_data.password_placeholder,
}

@allure.feature('Test Auth Page')
@allure.story('Test Auth Page')
@allure.title('User authorise test')
def test_user_authorise(authorisation_page):
    """Авторизация пользователя"""
    authorisation_page.open_page()
    authorisation_page.user_authorise(LOGIN, PASSWORD, authorisation_data)
