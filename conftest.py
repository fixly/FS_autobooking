from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest
import subprocess
import os


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """Генерирует отчет после всех тестов"""
    if os.path.exists("allure-results"):
        print("\nГенерация Allure отчета...")
        try:
            subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report", "--clean"], shell=True)
            print("Отчет сгенерирован в allure-report/")
            print("Для просмотра выполните: allure open allure-report")
        except FileNotFoundError:
            print("Allure не установлен. Установите его для генерации отчетов.")
            # pytest Tests/booking_test.py --alluredir=allure-results -v (Команда bash для запуска теста с сохранением результата)
            # allure generate allure-results -o allure-report --clean (Команда bash для генерации отчёта отдельно)
            # allure open allure-report (Команда bash для открытия отчёта отдельно)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Получаем результат выполнения теста
    outcome = yield
    rep = outcome.get_result()

    # Проверяем, что тест упал
    if rep.when == 'call' and rep.failed:
        # Получаем доступ к драйверу из фикстуры
        driver = item.funcargs.get('driver')
        if driver is not None:
            # Делаем скриншот и прикрепляем к Allure
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
