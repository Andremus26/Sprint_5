from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, AccountPageLocators, LoginPageLocators
from data_generator import generate_unique_email, generate_password

class TestLogout:
    def test_logout(self, driver, registered_user):
        email, password = registered_user  # используем ту же фикстуру из test_login
        # Вход в аккаунт
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(AccountPageLocators.ACCOUNT_INFO)
        )
        # Клик по кнопке "Выход"
        driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()
        # После выхода должна появиться кнопка "Войти" на главной
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        assert "login" in driver.current_url