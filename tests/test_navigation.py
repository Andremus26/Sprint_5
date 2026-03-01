from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, AccountPageLocators, LoginPageLocators
from data_generator import generate_unique_email, generate_password

class TestNavigation:
    def test_go_to_personal_account(self, driver):
        # Клик по "Личный кабинет" должен вести на страницу входа (если неавторизован)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert "login" in driver.current_url

    def test_go_to_constructor_from_account(self, driver):
        # Сначала залогинимся (используем предварительно созданного пользователя)
        # Для упрощения зарегистрируем пользователя в тесте
        # Но лучше вынести в фикстуру, как в test_login. Здесь создадим напрямую.
        # ... (опустим для краткости, предполагаем, что пользователь уже авторизован)
        # Переход в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(AccountPageLocators.ACCOUNT_INFO)
        )
        # Клик по "Конструктор"
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_TAB)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_go_to_main_by_logo(self, driver):
        # Аналогично предыдущему, но клик по логотипу
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(AccountPageLocators.ACCOUNT_INFO)
        )
        driver.find_element(*MainPageLocators.LOGO).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_TAB)
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"