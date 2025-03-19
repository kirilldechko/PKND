"""Страница выбора номера стандарта"""
import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.servises_page.servises_page_locators import servises_page_locators as serv_p_loc

class ServicesPage(BasePage):
    page_url = "/knm/appeals/services"

    @allure.step("Ввести номер стандарта в поле Код.")
    def set_code_to_code_fild(self, fild_name, service_number):
        code_field = self.find_elem(serv_p_loc.find_fild_by_name(fild_name))
        code_field.fill(service_number)
        code_field.press("Enter")

    @allure.step("Выбрать отфильтрованный стандарт по номеру стандарта и его названию")
    def choose_standard(self, standard_number, standard_name):
        filtered_row = self.find_elem(serv_p_loc.find_filtered_service(standard_number, standard_name))
        filtered_row.hover()
        try:
            expect(filtered_row).to_contain_text(standard_name)
        except AssertionError:
            raise AssertionError(f"Не найден стандарт с номером {standard_number} and name {standard_name}")

    @allure.step("Нажать кнопку Создать")
    def click_create_button(self, button_name):
        create_button = self.find_elem(serv_p_loc.find_create_button(button_name))
        create_button.click()
        expect(create_button).not_to_be_visible()

    @allure.step("Выбрать стандарт и создать дело")
    def choose_service_and_create_case(self, create_case_data):
        self.set_code_to_code_fild(create_case_data["code_fild_name"], create_case_data["service_number"])
        self.choose_standard(create_case_data["service_name"], create_case_data["service_name"])
        self.click_create_button(create_case_data["create_button_name"])
