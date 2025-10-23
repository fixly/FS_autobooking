import time
import datetime
import allure
import requests
from datetime import datetime
from Generator.generator import generated_person
from Generator.generator import FlightDate
from Generator.generator import random_city
from Pages.base_page import BasePage
from locators.booking_test_pages_locators import BookingPagesLocators as Locators
from selenium.webdriver.support.ui import WebDriverWait


class BookingTest(BasePage):

    @allure.tag("UI", "Booking", "Smoke")
    def client_way_booking_test(self):
        with allure.step("Генерация тестовых данных пассажира"):
            person = generated_person()
            time.sleep(11)

        with allure.step("Закрытие рекламного баннера"):
            banner = self.elements_is_visible(Locators.BannerClose)
            assert banner is not None, "Баннер не найден"
            banner.click()
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="banner_closed",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Выбор города отправления"):
            city_field = self.elements_is_visible(Locators.City)
            assert city_field is not None, "Поле выбора города не найдено"
            city_field.send_keys(random_city)
            time.sleep(1)

            city_list = self.elements_is_visible(Locators.CityList)
            assert city_list is not None, "Список городов не появился"
            city_list.click()

        with allure.step("Установка даты полета"):
            date_field = self.elements_is_visible(Locators.DateField)
            assert date_field is not None, "Поле даты не найдено"
            date_field.click()
            date_field.clear()
            date_field.send_keys(FlightDate)

            date_back_field = self.elements_is_visible(Locators.DateBacKFiled)
            assert date_back_field is not None, "Поле обратной даты не найдено"
            date_back_field.click()

        with allure.step("Подтверждение выбора дат"):
            submit_btn = self.elements_is_visible(Locators.Submit)
            assert submit_btn is not None, "Кнопка подтверждения не найдена"
            submit_btn.click()

            time.sleep(15)
            wait = WebDriverWait(self.driver, 15)
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        with allure.step("Поиск доступных рейсов"):
            search_submit = self.elements_is_visible(Locators.SearchSubmit)
            assert search_submit is not None, "Кнопка поиска не найдена"
            search_submit.click()

            time.sleep(10)
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="flight_search_results",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Выбор рейса"):
            first_continue = self.elements_is_visible(Locators.FirstContinue)
            assert first_continue is not None, "Первая кнопка продолжения не найдена"
            first_continue.click()

        with allure.step("Авторизация пользователя"):
            auth_button = self.elements_is_visible(Locators.AuthButton)
            assert auth_button is not None, "Кнопка авторизации не найдена"
            auth_button.click()

            email_field = self.elements_is_visible(Locators.Email)
            assert email_field is not None, "Поле email не найдено"
            email_field.send_keys('testfsmr19@yandex.ru')

            password_field = self.elements_is_visible(Locators.Password)
            assert password_field is not None, "Поле пароля не найдено"
            password_field.send_keys('SALK28fg')

            auth_submit = self.elements_is_visible(Locators.AuthSubmit)
            assert auth_submit is not None, "Кнопка подтверждения авторизации не найдена"
            auth_submit.click()

            time.sleep(1)
            wait = WebDriverWait(self.driver, 15)
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        with allure.step("Заполнение данных пассажира"):
            with allure.step("Ввод ФИО и даты рождения"):
                last_name = self.elements_is_visible(Locators.LastName)
                assert last_name is not None, "Поле фамилии не найдено"
                last_name.send_keys(person.LastName)

                first_name = self.elements_is_visible(Locators.FirstName)
                assert first_name is not None, "Поле имени не найдено"
                first_name.send_keys(person.FirstName)

                middle_name = self.elements_is_visible(Locators.MiddleName)
                assert middle_name is not None, "Поле отчества не найдено"
                middle_name.click()

                birth_date = self.elements_is_visible(Locators.BirthDate)
                assert birth_date is not None, "Поле даты рождения не найдено"
                birth_date.send_keys(person.BirthDate)

            with allure.step("Выбор пола"):
                gender = self.elements_is_visible(Locators.Gender)
                assert gender is not None, "Поле пола не найдено"
                gender.click()

                time.sleep(1)
                wait = WebDriverWait(self.driver, 15)
                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

                gender_random = self.elements_is_visible(Locators.GenderRandom)
                assert gender_random is not None, "Вариант пола не найден"
                gender_random.click()

            with allure.step("Ввод паспортных данных"):
                passport = self.elements_is_visible(Locators.Passport)
                assert passport is not None, "Поле паспорта не найдено"
                passport.send_keys(person.Passport)

        with allure.step("Заполнение контактных данных"):
            contact_last_name = self.elements_is_visible(Locators.ContactLastName)
            assert contact_last_name is not None, "Поле контактной фамилии не найдено"
            contact_last_name.send_keys('Тест')

            contact_first_name = self.elements_is_visible(Locators.ContactFirstName)
            assert contact_first_name is not None, "Поле контактного имени не найдено"
            contact_first_name.send_keys('Тест')

            contact_middle_name = self.elements_is_visible(Locators.ContactMiddleName)
            assert contact_middle_name is not None, "Поле контактного отчества не найдено"
            contact_middle_name.send_keys('Тест')

        with allure.step("Подтверждение условий оферты"):
            offer_agreement = self.elements_is_visible(Locators.OfferAgreement)
            assert offer_agreement is not None, "Чекбокс соглашения не найден"
            offer_agreement.click()
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="before_booking",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Выполнение бронирования"):
            Booking_agreement = self.elements_is_visible(Locators.BookingButton)
            assert Booking_agreement is not None, "Кнопка бронирования не найдена"
            Booking_agreement.click()
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="before_booking",
                attachment_type=allure.attachment_type.PNG
            )
        time.sleep(30)


class TelegramMessage(BasePage):

    def send_telegram_report(self):
        with allure.step("Отправка отчета в Telegram"):
            bot_token = "7957229168:AAFuNZTokayAlvtztj40bw9-sJaKbpN0j1E"
            chat_id = "1299266461"
            message = self.generate_report_message()

            # Отправка текстового сообщения
            text_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            requests.post(text_url, json={'chat_id': chat_id, 'text': message, 'parse_mode': 'HTML'})


    def generate_report_message(self):
                return f"""
        <b>📊 Отчет о бронировании</b>
        ────────────────
        <b>Направление:</b> {print('Москва')} - {print(Locators.City)}
                ────────────────
        <i>{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}</i>
        """
        # with allure.step("Завершение бронирования"):
    # <b>Статус:</b> {self.booking_data['status']}
    # <b>Пассажиров:</b> {self.booking_data['passengers']}
    # <b>Класс:</b> {self.booking_data['flight_type']}
    #  <b>Дата перелета:</b> {self.booking_data['flight_date']}
    #  <b>Длительность бронирования:</b> {self.['booking_duration']}
    # <b>Метод оплаты:</b> {self.booking_data['payment_method']}
    # booking_button = self.elements_is_visible(Locators.BookingButton)
    # assert booking_button is not None, "Кнопка бронирования не найдена"
    # booking_button.click()

            # Проверка успешного бронирования
            #time.sleep(30)
            #with allure.step("Проверка успешного завершения бронирования"):
            #    success_element = self.elements_is_visible(Locators.BookingSuccess, timeout=30)
            #    assert success_element is not None, "Бронирование не завершено успешно"
             #   assert "успешно" in success_element.text.lower(), "Не найдено подтверждение успешного бронирования"
              #  allure.attach(
               #     self.driver.get_screenshot_as_png(),
                #    name="booking_success",
                 #   attachment_type=allure.attachment_type.PNG
                #)
