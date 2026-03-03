import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import (
    MainPageLocators, LoginPageLocators, RegistrationPageLocators,
    RecoveryPageLocators, AccountPageLocators
)
from urls import MAIN_PAGE_URL, PROFILE_PAGE_URL

class TestLogin:
    def test_login_from_main_page(self, driver, registered_user):
        email, password = registered_user
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.current_url == MAIN_PAGE_URL

    def test_login_from_personal_account(self, driver, registered_user):
        email, password = registered_user
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AccountPageLocators.ACCOUNT_INFO)
        )
        assert driver.current_url == PROFILE_PAGE_URL

    def test_login_from_registration_form(self, driver, registered_user):
        email, password = registered_user
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        # Клик по ссылке «Войти» на странице регистрации
        driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.current_url == MAIN_PAGE_URL

    def test_login_from_password_recovery_form(self, driver, registered_user):
        email, password = registered_user
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.RECOVER_PASSWORD_LINK).click()
        driver.find_element(*RecoveryPageLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.current_url == MAIN_PAGE_URL