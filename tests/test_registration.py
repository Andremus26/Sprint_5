import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import RegistrationPageLocators, LoginPageLocators, MainPageLocators
from data_generator import generate_unique_email, generate_password

class TestRegistration:
    def test_registration_success(self, driver):
        # Переход на форму регистрации
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()

        # Заполнение формы
        name = "TestUser"
        email = generate_unique_email()
        password = generate_password(8)

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # После регистрации перекидывает на страницу входа. Ждем кнопку "Войти"
        success = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert success.is_displayed()

    def test_registration_wrong_password(self, driver):
        # Переход на форму регистрации
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()

        # Заполнение с коротким паролем
        name = "TestUser"
        email = generate_unique_email()
        password = generate_password(5)  # меньше 6 символов

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Проверяем появление сообщения об ошибке
        error = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        assert error.is_displayed()