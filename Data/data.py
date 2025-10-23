from dataclasses import dataclass


@dataclass
class Person:
    LastName: str = None
    FirstName: str = None
    Passport: str = None
    BirthDate: str = None


class Date:
    FlightDate: str = None


class City:
    CityName: str = None
