import dotenv
import os
import allure

from pages.organisation_page.organisation_page_data import organisation_page_data
from pages.application_page.application_page_data import application_page_data

# Загружаем переменные окружения из файла .env
dotenv.load_dotenv()

# Получаем значения переменных окружения
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# Тестовые данные
organisation_name = organisation_page_data.organisation[0]
application_name = application_page_data.application_name[0]


@allure.feature('Test Application Page')
@allure.story('Test Application Page')
@allure.title('Select application')
def test_select_application(authorisation_page, organisation_page, application_page):
    authorisation_page.open_page()
    authorisation_page.user_authorise(LOGIN, PASSWORD)
    organisation_page.select_organisation(organisation_name)
    application_page.select_application(application_name)