import random
from selenium.webdriver.common.by import By


# Генерация случайного пола
gender_options = ["Муж", "Жен"]
selected_gender = random.choice(gender_options)


class BookingPagesLocators:
    BannerClose = (By.XPATH, '//*[@id="popmechanic-form-86751"]/div[4]')
    City = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div/div/div/input')
    CityList = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div[1]/div')
    DateField = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/div/div/div[4]/div[2]/div/div/div/div/input')
    DateBacKFiled = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/div/div/div[5]/div[2]/div/div/div/div/input')
    Submit = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/div/div/button')
    SearchSubmit = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[3]/div/div/div[2]/div[2]')
    FirstContinue = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[6]/div[1]/div[2]/div/div[2]/div[7]')
    AuthButton = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[3]/div/div/div[2]/a')
    Email = (By.XPATH, '//*[@id="email"]')
    Password = (By.XPATH, '//*[@id="password"]')
    AuthSubmit = (By.XPATH, '//*[@id="app"]/div/header/div[1]/div[2]/div/div/div/div[3]/div/form/div[4]/input')
    LastName = (By.CSS_SELECTOR, 'input[data-cy="lastName"]')
    FirstName = (By.CSS_SELECTOR, 'input[data-cy="firstName"]')
    MiddleName = (By.XPATH, '//*[@id="ADULT0tourist_form"]/div[3]/div/label')
    BirthDate = (By.XPATH, '//*[@id="date"]')
    Gender = (By.CSS_SELECTOR, 'div[class="select-parent dropdown-select__tags"]')
    GenderRandom = (By.XPATH, f"//li[contains(@class, 'dropdown-select__element') and contains(text(), '{selected_gender}')]")
    Passport = (By.CSS_SELECTOR, 'input[data-cy="documentInfo"]')
    ContactLastName = (By.CSS_SELECTOR, '#lastName')
    ContactFirstName = (By.CSS_SELECTOR, '#firstName')
    ContactMiddleName = (By.CSS_SELECTOR, '#middleName')
    OfferAgreement = (By.XPATH, '//*[@id="start_contacts_block"]/div[2]/label/p/span')
    BookingButton = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[6]/div[1]/div[2]/div/div[2]/div[7]')
    SmsInformButton = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/div[2]/div[1]/div[2]/button')
    FirstPaymentButton = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/button')
    SBpPaymentButton = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]')
    RussianCard = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]')
    GateLineCard = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[3]')
    SecondPaymentButton = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[2]/div/button')
