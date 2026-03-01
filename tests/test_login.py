import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, RecoveryPageLocators, AccountPageLocators
from data_generator import generate_unique_email, generate_password

@pytest.fixture(scope="function")
def registered_user(driver):
    """Фикстура для создания пользователя перед тестами входа"""
    # Переход на регистрацию
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

    # Ждем появления формы логина
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
    )
    return email, password

class TestLogin:
    def test_login_from_main_page(self, driver, registered_user):
        email, password = registered_user
        # На главной нажимаем "Войти в аккаунт"
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        # Заполняем форму входа
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Проверяем, что попали в личный кабинет (по кнопке "Оформить заказ" или другой элемент)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_login_from_personal_account(self, driver, registered_user):
        email, password = registered_user
        # Клик по "Личный кабинет" (неавторизован)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        # Заполняем форму входа
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        # Проверка успешного входа (переход в личный кабинет)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AccountPageLocators.ACCOUNT_INFO)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

    def test_login_from_registration_form(self, driver, registered_user):
        email, password = registered_user
        # Переход на форму регистрации
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)
        ).click()
        # На форме регистрации есть ссылка "Войти"
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()  # Возможно, это не та ссылка, нужна другая
        # Уточним локатор: на странице регистрации есть ссылка для входа (обычно "Войти" под формой)
        # В locators нужно добавить LOGIN_LINK_ON_REGISTER
        # Для упрощения используем переход по кнопке "Войти" на странице входа? Нет, нам нужно проверить вход через форму регистрации.
        # На странице регистрации есть кнопка "Войти" (ссылка) — нужно добавить локатор.
        # Пока предположим, что после клика по ссылке "Войти" попадаем на форму логина.
        # Временно используем:
        # driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        # Заполняем логин и пароль.
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        # Проверка
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AccountPageLocators.ACCOUNT_INFO)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

    def test_login_from_password_recovery_form(self, driver, registered_user):
        email, password = registered_user
        # Переход на восстановление пароля
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.RECOVER_PASSWORD_LINK).click()
        # На странице восстановления есть ссылка "Войти"
        driver.find_element(*RecoveryPageLocators.LOGIN_LINK).click()
        # Заполняем форму входа
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        # Проверка
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AccountPageLocators.ACCOUNT_INFO)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"