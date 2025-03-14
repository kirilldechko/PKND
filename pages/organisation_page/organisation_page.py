import allure

from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.organisation_page.organisation_page_locators import organisation_page_loc as sol
from pages.application_page.application_page_data import application_page_data as app_page_data


class OrganisationPage(BasePage):
    page_url = "/select-organization"

    @allure.step("Выбор КНО")
    def select_organisation(self, kno_and_knm_data):
        organisation = self.find_elem(sol.find_organisation_name(kno_and_knm_data["organisation_name"]))
        organisation.click()
        try:
            expect(self.page).to_have_url(app_page_data.page_url)
        except AssertionError:
            raise AssertionError("Не удалось выполнить переход на страницу выбора КНД")



