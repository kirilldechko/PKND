"""Страница выбора организации"""
import allure

from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.organisation_page.organisation_page_locators import organisation_page_loc as sol
from pages.application_page.application_page_data import application_page_data as app_page_data


class OrganisationPage(BasePage):
    page_url = "/select-organization"

    @allure.step("Проверить что пользователь на странице выбора КНО")
    def check_organisation_page(self, page_name):
        page_name = self.find_elem(sol.find_page_name(page_name))
        expect(page_name).to_be_visible()

    @allure.step("Выбор КНО")
    def select_organisation(self, kno_name):
        organisation = self.find_elem(sol.find_organisation_name(kno_name))
        organisation.click()
        try:
            expect(self.page).to_have_url(app_page_data.page_url)
        except AssertionError:
            raise AssertionError("Не удалось выполнить переход на страницу выбора КНД")

    @allure.step("Проверить страницу и выбрать КНО")
    def check_page_and_choose_organisation(self, organisation_page_data):
        self.check_organisation_page(organisation_page_data["organisation_page_name"])
        self.select_organisation(organisation_page_data["organisation_name"])



