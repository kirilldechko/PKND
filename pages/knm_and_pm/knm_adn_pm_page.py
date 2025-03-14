import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.knm_and_pm.knm_and_pm_page_data import knm_and_pm_page_data as knm_data
from pages.knm_and_pm.knm_and_pm_page_locators import knm_and_pn_page_loc


class KnmAndPmPage(BasePage):
    page_url = "/knm/appeals"

    @allure.step("Нажать кнопку добавить дело.")
    def press_add_case_button(self, button_name):
        add_case_button = self.find_elem(knm_and_pn_page_loc.find_add_case_button(button_name))
        add_case_button.click()
        code_field = self.find_elem(knm_and_pn_page_loc.find_text_fild_by_placeholder(knm_data.code_fild_name))
        expect(code_field).to_be_visible()

    @allure.step("Ввести номер стандарта в поле Код.")
    def set_code_to_code_fild(self, standard_number):
        code_field = self.find_elem(knm_and_pn_page_loc.find_text_fild_by_placeholder(knm_data.code_fild_name))
        code_field.fill(standard_number)
        code_field.press("Enter")

    @allure.step("Выбрать отфильтрованный стандарт по номеру стандарта и его названию")
    def choose_standard(self, standard_number, standard_name):
        filtered_row = self.find_elem(knm_and_pn_page_loc.find_filtered_st(standard_number, standard_name))
        filtered_row.hover()
        try:
            expect(filtered_row).to_contain_text(standard_name)
        except AssertionError:
            raise AssertionError(f"Не найден стандарт с номером {standard_number} and name {standard_name}")

    @allure.step("Нажать кнопку Создать")
    def click_create_button(self, button_name):
        create_button = self.find_elem(knm_and_pn_page_loc.find_create_button(button_name))
        create_button.click()
        expect(create_button).not_to_be_visible()

    @allure.step("Проверяем что пользователь находится на странице создания дела")
    def check_create_page_name(self, page_name):
        create_page_name = self.find_elem(knm_and_pn_page_loc.find_create_page_name(page_name))
        expect(create_page_name).to_be_visible(timeout=10000)
        expect(create_page_name).to_have_text(page_name)

    @allure.step("Выбрать значение в справочнике")
    def select_a_value_from_directory(self, directory_name, value):
        find_directory=self.find_elem(knm_and_pn_page_loc.find_directory_by_name(directory_name))
        find_directory.click()
        find_directory_value=self.find_elem(knm_and_pn_page_loc.find_directory_value(value))
        find_directory_value.click()
        check_directory_value = self.find_elem(knm_and_pn_page_loc.find_directory_by_name(directory_name))
        try:
            expect(check_directory_value).to_have_value(value)
        except AssertionError:
            raise AssertionError(f"Ошибка при выборе значения в справочнике {directory_name}")

    @allure.step("Заполнить текстовое поле")
    def enter_value_to_text_fild(self, fild_name, value):
        text_fild_name = self.find_elem(knm_and_pn_page_loc.find_text_fild_by_name(fild_name))
        text_fild_name.fill(value)
        try:
            expect(text_fild_name).to_have_value(value)
        except AssertionError:
            raise AssertionError(f"Ошибка при заполнении поля {text_fild_name}")

    @allure.step("Выбрать дату")
    def send_date(self, date_fild_name, date, period=None):
        date_fild = self.find_elem(knm_and_pn_page_loc.find_date_fild(date_fild_name))
        date_fild.fill(date)
        try:
            expect(date_fild).to_have_value(date)
        except AssertionError:
            raise AssertionError(f"Ошибка при заполнении поля {date_fild}")

    @allure.step("Выбрать дату")
    def send_time(self, time_fild_name, time, period=None):
        time_fild = self.find_elem(knm_and_pn_page_loc.find_time_fild(time_fild_name))
        time_fild.fill(time)
        try:
            expect(time_fild).to_have_value(time)
        except AssertionError:
            raise AssertionError(f"Ошибка при заполнении поля {time_fild}")

    @allure.step("Очистить значение справочника")
    def clean_dictionary_value(self, dictionary_name):
        clean_elem = self.find_elem(knm_and_pn_page_loc.find_delete_element(dictionary_name))
        clean_elem.click()

    @allure.step("Нажать кнопку Сохранить")
    def press_save_button(self, button_name, reg_button_name):
        save_button = self.find_elem(knm_and_pn_page_loc.find_save_button(button_name))
        save_button.click()
        registration_button = self.find_elem(knm_and_pn_page_loc.find_reg_button(reg_button_name))
        try:
            expect(registration_button).to_be_visible()
        except AssertionError:
            raise AssertionError(f"После сохранения не отобразилась кнопка {reg_button_name}")

    @allure.step("Создать дело (Указать Стандарт > Создать дело)")
    def create_case(self, create_case_data, kno_and_knm_data ):
        """Указать Номер стандарта, кнопку Добавить Дело, полное наименование стандарта, кнопку Создать"""
        self.press_add_case_button(create_case_data["add_case_button"])
        self.set_code_to_code_fild(kno_and_knm_data["st_num"])
        self.choose_standard(kno_and_knm_data["st_num"], kno_and_knm_data["st_full_name"])
        self.click_create_button(create_case_data["create_button"])
        self.check_create_page_name(kno_and_knm_data["st_full_name"])

    @allure.step("Заполнить поля вкладки Общие данные")
    def fill_in_the_general_information(self, general_information, create_case_data):
        self.select_a_value_from_directory(general_information['directory_type_of_state_control'],
                                           general_information['type_of_state_control_value'])
        self.select_a_value_from_directory(general_information['directory_knm_foundation'],
                                           general_information['knm_foundation_value'])
        self.enter_value_to_text_fild(general_information['another_passport_link_fild'],
                                      general_information['random_word'])
        self.send_date(general_information['beginning_knm_date_fild'], general_information['current_date'])
        self.send_time(general_information['beginning_knm_time_fild'], general_information['current_time'])
        self.send_date(general_information['ending_knm_date_fild'], general_information['current_date'])
        self.send_time(general_information['ending_knm_time_fild'], general_information['current_time'])
        self.enter_value_to_text_fild(general_information['knm_date_period_fild_name'],
                                      general_information['knm_date_period'])
        self.enter_value_to_text_fild(general_information['knm_time_period_fild_name'],
                                      general_information['knm_time_period'])
        self.clean_dictionary_value(general_information['need_for_coordination'])
        self.select_a_value_from_directory(general_information['need_for_coordination'],
                                           general_information['need_for_coordination_values'])
        self.select_a_value_from_directory(general_information['post_fild'], general_information['post'])
        self.press_save_button(create_case_data['save_button'], general_information['reg_button'])
        self.select_a_value_from_directory(general_information['directory_type_of_state_control'],
                                           general_information['type_of_state_control_value'])
        self.press_save_button(create_case_data['save_button'], general_information['reg_button'])

    @allure.step("Переход на вкладку левого меню")
    def go_to_the_left_tab_by_name(self, left_tab_name):
        tab_name = self.find_elem(knm_and_pn_page_loc.find_left_menu_button(left_tab_name))
        tab_name.click()

    @allure.step("Нажать кнопку Добавить")
    def press_add_button(self, button_name):
        add_button = self.find_elem(knm_and_pn_page_loc.find_add_button(button_name))
        add_button.click()

