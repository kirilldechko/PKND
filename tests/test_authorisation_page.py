import dotenv
import os
import allure

# Загружаем переменные окружения из файла .env
dotenv.load_dotenv()

# Получаем значения переменных окружения
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


@allure.feature('Test Auth Page')
@allure.story('Test Auth Page')
@allure.title('User authorise test')
def test_user_authorise(authorisation_page):
    """Авторизация пользователя"""
    authorisation_page.open_page()
    authorisation_page.user_authorise(LOGIN, PASSWORD)