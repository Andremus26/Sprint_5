import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from data_generator import generate_unique_email, generate_password

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def registered_user(driver):
    """Создание пользователя, возврат email и пароля"""
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
    ).click()

    name = "TestUser"
    email = generate_unique_email()
    password = generate_password(8)

    driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
    )
    return email, password