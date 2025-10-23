import allure
from Pages.booking_test_pages import BookingTest
from Pages.booking_test_pages import TelegramMessage
from conftest import driver


@allure.suite("BookingSmoke")
class TestBookingPages:

    @allure.feature("Check Booking")
    def test_booking_pages(self, driver):
        try:
            booking_test = BookingTest(driver, 'https://fstravel.com/avia')
            booking_test.open()
            booking_test.client_way_booking_test()
        finally:
            telegram_test = TelegramMessage(driver, 'https://fstravel.com/avia')
            telegram_test.open()
            # Сообщение в терминал о генерации и переходе на страницу отчёта allure
            print("\nAllure результаты сохранены в allure-results/")
            print("Для генерации отчета выполните:")
            print("allure generate allure-results -o allure-report --clean")
            print("allure open allure-report")
