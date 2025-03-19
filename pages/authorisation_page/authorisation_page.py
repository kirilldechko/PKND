"""Страница авторизации пользователя"""
import allure

from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.authorisation_page.auth_page_locators import autorization_page_loc as auth_page_loc
from pages.organisation_page.organisation_page_data import organisation_page_data as sel_page_data


class AuthorisationPage(BasePage):
    page_url = "/login"

    @allure.step("Проверка наименования страницы входа в информационную систему")
    def check_the_login_page_name(self, page_name):
        search_page_name = self.find_elem(auth_page_loc.find_page_name(page_name))
        try:
            expect(search_page_name).to_have_text(page_name)
        except AssertionError:
            raise AssertionError(f"Имя страницы не соответствует тестовому имени: {page_name}.")

    @allure.step("Выбрать чекбокс, на странице авторизации")
    def choose_the_checkbox(self, check_box_name, enter_button_name):
        search_check_box = self.find_elem(auth_page_loc.find_check_box_by_name(check_box_name))
        search_check_box.click()
        search_enter_button = self.find_elem(auth_page_loc.find_enter_button(enter_button_name))
        try:
            expect(search_enter_button).to_have_text(enter_button_name)
        except AssertionError:
            raise AssertionError(f"Название кнопки не соответствует: {enter_button_name}.")

    @allure.step("Заполнить поле логин")
    def fill_the_login_fild(self, login_placeholder, login):
        search_login_fild = self.find_elem(auth_page_loc.find_login_fild(login_placeholder))
        search_login_fild.fill(login)
        try:
            expect(search_login_fild).to_have_value(login)
        except AssertionError:
            raise AssertionError(f"Данные в поле Логин не соответствуют тестовым: {login}.")

    @allure.step("Заполнить поле пароль")
    def fill_the_pass_fild(self, password_placeholder, password):
        search_pass_fild = self.find_elem(auth_page_loc.find_password_fild(password_placeholder))
        search_pass_fild.fill(password)
        try:
            expect(search_pass_fild).to_have_value(password)
        except AssertionError:
            raise AssertionError(f"Данные в поле Пароль не соответствуют тестовым: {password}.")

    @allure.step("Нажать кнопку Войти в систему")
    def press_enter_button(self, button_name):
        search_enter_button = self.find_elem(auth_page_loc.find_enter_button(button_name))
        search_enter_button.click()
        # Проверяем, что произошел переход на другую страницу
        expect(self.page).to_have_url(sel_page_data.page_url)

    @allure.step("Авторизация пользователя")
    def user_authorise(self, login, password, auth_data):
        self.check_the_login_page_name(auth_data["page_name"])
        self.choose_the_checkbox(auth_data["check_box_fild_name"], auth_data["enter_button_name"])
        self.fill_the_login_fild(auth_data["login_placeholder"], login)
        self.fill_the_pass_fild(auth_data["password_placeholder"], password)
        self.press_enter_button(auth_data["enter_button_name"])
