from time import sleep

import dotenv
import os
import allure

from pages.organisation_page.organisation_page_data import organisation_page_data
from pages.application_page.application_page_data import application_page_data
from pages.authorisation_page.auth_page_data import authorisation_page_data as auth_p_data
from pages.appeals_page.appeals_page_data import appeals_page_data as app_p_data

# Загружаем переменные окружения из файла .env
dotenv.load_dotenv()

# Получаем значения переменных окружения
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# Тестовые данные на странице выбора КНО
application_name = application_page_data.application_names["knm_and_pm"]

# Тестовые данные на странице авторизации
authorisation_data = {
    "page_name": auth_p_data.page_name,
    "enter_button_name": auth_p_data.enter_button_name,
    "check_box_fild_name": auth_p_data.check_box_fild_name,
    "login_placeholder": auth_p_data.login_placeholder,
    "password_placeholder": auth_p_data.password_placeholder,
}
# Тестовые данные на странице выбора организации
organisation_page_data = {
"organisation_name": organisation_page_data.organisation[0],
"organisation_page_name": organisation_page_data.organisation_page_name,
}

# Тестовые данные на странице создания обращения
add_case_button_name = app_p_data.add_case_button_name

@allure.feature('Test Appeals Page')
@allure.story('Test Appeals Page')
@allure.title('Create Appeals')
def test_select_appeals(authorisation_page, organisation_page, application_page, appeals_page):
    authorisation_page.open_page()
    authorisation_page.user_authorise(LOGIN, PASSWORD, authorisation_data)
    organisation_page.check_page_and_choose_organisation(organisation_page_data)
    application_page.select_application(application_name)
    appeals_page.press_add_case_button(add_case_button_name)
