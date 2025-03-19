import dotenv
import os
import allure

from pages.organisation_page.organisation_page_data import organisation_page_data
from pages.authorisation_page.auth_page_data import authorisation_page_data as auth_p_data

# Загружаем переменные окружения из файла .env
dotenv.load_dotenv()

# Получаем значения переменных окружения
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# Тестовые данные страницы авторизации
authorisation_data = {
    "page_name": auth_p_data.page_name,
    "enter_button_name": auth_p_data.enter_button_name,
    "check_box_fild_name": auth_p_data.check_box_fild_name,
    "login_placeholder": auth_p_data.login_placeholder,
    "password_placeholder": auth_p_data.password_placeholder,
}
# Тестовые данные на странице выбора КНО
organisation_page_data = {
"organisation_name": organisation_page_data.organisation[0],
"organisation_page_name": organisation_page_data.organisation_page_name,
}



@allure.feature('Test Organisation Page')
@allure.story('Test Organisation Page')
@allure.title('Select organisation')
def test_select_organisation(authorisation_page, organisation_page):
    """Выбор и переход на страницу КНО"""
    authorisation_page.open_page()
    authorisation_page.user_authorise(LOGIN, PASSWORD, authorisation_data)
    organisation_page.check_page_and_choose_organisation(organisation_page_data)