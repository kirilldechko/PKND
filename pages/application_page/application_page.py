"""Страница выбора надзорной деятельности"""
import allure

from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.application_page.application_page_locators import application_page_loc


class ApplicationPage(BasePage):
    page_url = "/select-application"

    @allure.step("Выбор надзорной деятельности.")
    def select_application(self, application_names):
        found_application = self.find_elem(application_page_loc.application_path(application_names))
        found_application.click()
        try:
            expect(self.find_elem(application_page_loc.crumbs_application_name(application_names)))
        except AssertionError:
            raise AssertionError(f"Не удалось найти вид надзорной деятельности: {application_names}.")
