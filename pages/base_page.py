"""файл base_page.py содержит базовые методы для работы с элементами страниц"""
from playwright.sync_api import Page

class BasePage:
    """Базовый класс для всех страниц"""
    base_url = "https://pknd-test.mos.ru"
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):  # Функция для открытия страницы
        self.page.goto(f'{self.base_url}{self.page_url}', timeout=90000)

    def find_elem(self, locator):
        return self.page.locator(locator)  # функция поиска элемента по локатору

    def select_value_from_guide(self, guide_name, value=None):
        self.find_elem()
