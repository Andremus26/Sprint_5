from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, AccountPageLocators, LoginPageLocators
from urls import LOGIN_PAGE_URL, MAIN_PAGE_URL, PROFILE_PAGE_URL

class TestNavigation:
    def test_go_to_personal_account(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert driver.current_url == LOGIN_PAGE_URL

    def test_go_to_constructor_from_account(self, driver, registered_user):
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
        # Клик по «Конструктор»
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_TAB)
        )
        assert driver.current_url == MAIN_PAGE_URL

    def test_go_to_main_by_logo(self, driver, registered_user):
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
        # Клик по логотипу
        driver.find_element(*MainPageLocators.LOGO).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_TAB)
        )
        assert driver.current_url == MAIN_PAGE_URL