import dotenv
import os
import allure
from faker import Faker
from time import sleep


fake = Faker()

from conftest import knm_and_pm_page
from pages.organisation_page.organisation_page_data import organisation_page_data
from pages.knm_and_pm.knm_and_pm_page_data import knm_and_pm_page_data
from pages.application_page.application_page_data import application_page_data
from pages.pages_data  import standart_numbers

# Загружаем переменные окружения из файла .env
dotenv.load_dotenv()

# Получаем значения переменных окружения
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

# Тестовые данные КНО и КНМ
kno_and_knm_data = {
"organisation_name": organisation_page_data.organisation[0], # Название организации
"application_name": application_page_data.application_name[0], # Вид КНМ
"st_num": standart_numbers.standart_numbers[0], # Номер cтандарта
"st_full_name": knm_and_pm_page_data.standard_full_name, # Наименование стандарта
}

# Тестовые данные Создание дела
create_case_data = {
"add_case_button": knm_and_pm_page_data.add_case_button_name, # кнопка Добавить дело
"create_button": knm_and_pm_page_data.create_button_name, # кнопка Создать
"save_button": knm_and_pm_page_data.save_button_name, # кнопка Сохранить
"create_page_name": knm_and_pm_page_data.create_page_name, # Создание дела
}

# Тестовые данные (Общие данные)
general_information = {
"reg_button": knm_and_pm_page_data.reg_button_name, # кнопка Регистрация
"directory_type_of_state_control": knm_and_pm_page_data.directory[0], # поле Вид государственного контроля
"type_of_state_control_value": knm_and_pm_page_data.type_of_state_control_value[0], # значение в поле Вид государственного контроля
"directory_knm_foundation": knm_and_pm_page_data.directory[1], # справочник Основание КНМ (ЕРВК)
"knm_foundation_value": knm_and_pm_page_data.knm_foundation_value[0], # значение в справочнике Основание КНМ (ЕРВК)
"another_passport_link_fild": knm_and_pm_page_data.text_fild_name[0], # поле Ссылка на другой паспорт КНМ
"random_word": fake.word(), # случайное слово
"current_date": knm_and_pm_page_data.current_date, # текущая дата
"beginning_knm_date_fild": knm_and_pm_page_data.beginning_knm_date_fild_name, # поле Дата начала КНМ
"beginning_knm_time_fild": knm_and_pm_page_data.beginning_knm_time_fild_name, # поле Время начала КНМ
"current_time": knm_and_pm_page_data.current_time, # текущее время
"ending_knm_date_fild": knm_and_pm_page_data.ending_knm_date_fild_name, # поле Дата окончания КНМ
"ending_knm_time_fild": knm_and_pm_page_data.ending_knm_date_time_name, # поле Время окончания КНМ
"knm_date_period": knm_and_pm_page_data.knm_date_period, # значение для поля Срок проведения (дней)
"knm_time_period": knm_and_pm_page_data.knm_time_period, # значение для поля Срок непосредственного взаимодействия (часов)
"need_for_coordination": knm_and_pm_page_data.need_for_coordination_fild_name, # поле Необходимость согласования
"need_for_coordination_values": knm_and_pm_page_data.need_for_coordination_values[1], # значение для поля Необходимость согласования
"post": knm_and_pm_page_data.post[0], # значение поля должность
"post_fild": knm_and_pm_page_data.post_fild_name, # поле Должность
"left_menu_button": knm_and_pm_page_data.left_menu_buttons, # кнопки левого меню
"add_button": knm_and_pm_page_data.add_button_name, # кнопка Добавить
"knm_date_period_fild_name": knm_and_pm_page_data.knm_date_period_fild_name, # поле Срок проведения (дней)
"knm_time_period_fild_name": knm_and_pm_page_data.knm_time_period_fild_name, # поле Срок непосредственного взаимодействия (часов)
}

@allure.feature('Test Application Page')
@allure.story('Test Application Page')
@allure.title('Select application')
def test_fill_general_information(authorisation_page, organisation_page, application_page, knm_and_pm_page):
    authorisation_page.open_page()
    authorisation_page.user_authorise(LOGIN, PASSWORD) # авторизация пользователя
    organisation_page.select_organisation(kno_and_knm_data) # выбор КНО
    application_page.select_application(kno_and_knm_data) # выбор КНД
    knm_and_pm_page.create_case(create_case_data, kno_and_knm_data) # Создать дело
    knm_and_pm_page.fill_in_the_general_information(general_information, create_case_data) # Заполнить общие данные
    sleep(10)

