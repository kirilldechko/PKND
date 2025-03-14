import allure

from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.authorisation_page.auth_page_locators import autorization_page_loc as auth_page_loc
from pages.organisation_page.organisation_page_data import organisation_page_data as sel_page_data
from pages.authorisation_page.auth_page_data import authorisation_page_data as ap_data


class AuthorisationPage(BasePage):
    page_url = "/login"

    @allure.step("Проверка наименования страницы входа в информационную систему")
    def check_the_login_page_name(self, page_name):
        search_page_name = self.find_elem(auth_page_loc.page_name_loc)
        try:
            expect(search_page_name).to_have_text(page_name)
        except AssertionError:
            raise AssertionError(f"Имя страницы не соответствует тестовому имени: {page_name}.")

    @allure.step("Выбрать и проверить чекбокс, на странице авторизации")
    def choose_the_checkbox(self, button_name):
        search_check_box = self.find_elem(auth_page_loc.check_box_loc)
        search_check_box.click()
        search_enter_button = self.find_elem(auth_page_loc.enter_button_loc)
        try:
            expect(search_enter_button).to_have_text(button_name)
        except AssertionError:
            raise AssertionError(f"Название кнопки не соответсвует тестовому: {button_name}.")

    @allure.step("Заполнить поле логин")
    def fill_the_login_fild(self, login_name):
        search_login_fild = self.find_elem(auth_page_loc.login_fild_loc)
        search_login_fild.fill(login_name)
        try:
            expect(search_login_fild).to_have_value(login_name)
        except AssertionError:
            raise AssertionError(f"Данные в поле Логин не соответствуют тестовым: {login_name}.")

    @allure.step("Заполнить поле пароль")
    def fill_the_pass_fild(self, password):
        search_pass_fild = self.find_elem(auth_page_loc.password_fild_loc)
        search_pass_fild.fill(password)
        try:
            expect(search_pass_fild).to_have_value(password)
        except AssertionError:
            raise AssertionError(f"Данные в поле Пароль не соответствуют тестовым: {password}.")

    @allure.step("Нажать кнопку 'Войти в систему' и проверить что открыта страница с новым URL")
    def press_enter_button(self, button_name=None):
        search_enter_button = self.find_elem(auth_page_loc.enter_button_loc)
        search_enter_button.click()
        # Проверяем, что произошел переход на другую страницу
        expect(self.page).to_have_url(sel_page_data.page_url)

    @allure.step("Авторизация пользователя")
    def user_authorise(self, login_name, password):
        self.choose_the_checkbox(ap_data.authorisation_page_enter_button_name)
        self.fill_the_login_fild(login_name)
        self.fill_the_pass_fild(password)
        self.press_enter_button(ap_data.authorisation_page_enter_button_name)
