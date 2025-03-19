import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.subject_page.subject_page_locators import subjects_page_locators as sub_p_loc



class SubjectPage(BasePage):
    page_url = "/selecting/global-subjects/global"

    @allure.step("Очистить поле Вид КНД")
    def clear_fild(self, fild_name):
        find_fild_by_name = self.find_elem(sub_p_loc.find_fild_path_in_left_menu_by_name(fild_name))
        if find_fild_by_name is not None:
            find_fild_by_name.clear()
            expect(find_fild_by_name).to_have_value("")

    @allure.step("Выполнить поиск субъекта по наименованию")
    def find_subject_by_name(self, search_fild_name, subject_name):
        search_fild = self.find_elem(sub_p_loc.find_search_fild_path(search_fild_name))
        search_fild.click()
        search_fild.fill(subject_name)
        search_fild.press("Enter")
        subject_check_box = self.find_elem(sub_p_loc.find_subject_check_box_path(subject_name))
        subject_check_box.click()
        expect(subject_check_box).not_to_be_visible()

    # @allure.step("Выбрать субъект контроля")
    # def choose_control_subject(self, subject_data):
    #     self.clear_fild(subject_data[]fild_name)

