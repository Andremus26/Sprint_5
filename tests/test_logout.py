from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, AccountPageLocators, LoginPageLocators
from urls import LOGIN_PAGE_URL

class TestLogout:
    def test_logout(self, driver, registered_user):
        email, password = registered_user
        # Вход
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(AccountPageLocators.ACCOUNT_INFO)
        )
        # Выход
        driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()
        # Проверка, что попали на страницу входа
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        assert driver.current_url == LOGIN_PAGE_URL