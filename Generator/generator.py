from Data.data import Person
from faker import Faker
import random
from datetime import datetime
from dateutil.relativedelta import relativedelta


faker_ru = Faker('Ru')
faker_en = Faker('En')


def generated_person():
    return Person(
        LastName=faker_en.last_name(),
        FirstName=faker_en.first_name(),
        Passport=faker_ru.passport_number(),
        BirthDate=faker_ru.date_of_birth().strftime("%d.%m.%Y")
    )


# Генерация даты из списка
cities = ["Сочи", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]

# Выбираем случайный город
random_city = random.choice(cities)


# Генерация даты с помощью dateutil
current_date = datetime.now()
future_date = current_date + relativedelta(months=3)
formatted_date = future_date.strftime("%d-%m-%Y")
FlightDate = formatted_date


# Генерация даты с помощью dateutil
# current_date = datetime.now()
# future_date = current_date + relativedelta(months=3)
# formatted_date = future_date.strftime("%d-%m-%Y")
# FlightDate = formatted_date #
