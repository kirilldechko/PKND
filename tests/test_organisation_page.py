import dotenv
import os
import allure

from pages.organisation_page.organisation_page_data import organisation_page_data

# Загружаем переменные окружения из файла .env
dotenv.load_dotenv()

# Получаем значения переменных окружения
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# Тестовые данные
organisation_name = organisation_page_data.organisation[0]


@allure.feature('Test Organisation Page')
@allure.story('Test Organisation Page')
@allure.title('Select organisation')
def test_select_organisation(authorisation_page, organisation_page):
    """Выбор и переход на страницу КНО"""
    authorisation_page.open_page()
    authorisation_page.user_authorise(LOGIN, PASSWORD)
    organisation_page.select_organisation(organisation_name)