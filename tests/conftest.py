import pytest
from playwright.sync_api import sync_playwright

from pages.appeals_page.appeals_page import AppealsPage
from pages.authorisation_page.authorisation_page import AuthorisationPage
# from pages.knm_and_pm.knm_adn_pm_page import KnmAndPmPage
from pages.organisation_page.organisation_page import OrganisationPage
from pages.application_page.application_page import ApplicationPage
from pages.servises_page.services_page import ServicesPage
from pages.subject_page.subject_page import SubjectPage



# Фикстура для настройки контекста браузера (например, размер окна, игнорирование HTTPS-ошибок).
# Эта фикстура выполняется один раз за всю сессию тестов (scope="session").
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,  # Сохраняем существующие аргументы контекста.
        "viewport": {"width": 1920, "height": 1080},  # Устанавливаем размер окна браузера.
        "ignore_https_errors": True  # Игнорируем ошибки HTTPS (например, для тестирования сайтов с самоподписанными сертификатами).
    }

# Фикстура для управления жизненным циклом браузера.
# Эта фикстура выполняется один раз для всего модуля тестов (scope="module").
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:  # Инициализируем Playwright.
        browser = p.chromium.launch(headless=False)  # Запускаем браузер Chromium в видимом режиме.
        yield browser  # Возвращаем браузер для использования в тестах.
        browser.close()  # Закрываем браузер после завершения всех тестов в модуле.

# Фикстура для управления жизненным циклом страницы.
# Эта фикстура выполняется для каждого теста (scope="function").
@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()  # Создаем новую страницу в браузере.
    yield page  # Возвращаем страницу для использования в тесте.
    page.close()  # Закрываем страницу после завершения теста.

@pytest.fixture
def authorisation_page(page):
    return AuthorisationPage(page)

@pytest.fixture
def organisation_page(page):
    return OrganisationPage(page)

@pytest.fixture
def application_page(page):
    return ApplicationPage(page)

@pytest.fixture
def knm_and_pm_page(page):
    return KnmAndPmPage(page)

@pytest.fixture
def subject_page(page):
    return SubjectPage(page)

@pytest.fixture
def appeals_page(page):
    return AppealsPage(page)

@pytest.fixture
def service_page(page):
    return ServicesPage(page)