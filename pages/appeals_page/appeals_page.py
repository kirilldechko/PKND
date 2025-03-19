"""Страница 'Обращения' - создание обращения (дела)..."""
import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.appeals_page.appeals_page_locators import appeals_page_locators as app_p_loc


class AppealsPage(BasePage):
    page_url = "/knm/appeals"

    @allure.step("Нажать кнопку Добавить дело")
    def press_add_case_button(self, add_case_button_name):
        add_case_button = self.find_elem(app_p_loc.find_add_case_button(add_case_button_name))
        add_case_button.click()
        expect(add_case_button).not_to_be_visible()

