from selenium.webdriver.common.by import By

class MainPageLocators:
    # Главная страница
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка входа на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип Stellar Burgers
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Вкладка "Начинки"
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # Активная вкладка

class LoginPageLocators:
    # Страница входа
    EMAIL_INPUT = (By.NAME, "name")  # Поле Email
    PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле Пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка на регистрацию
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка восстановления

class RegistrationPageLocators:
    # Страница регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле Имя
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле Пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об ошибке пароля

class RecoveryPageLocators:
    # Страница восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" на странице восстановления

class AccountPageLocators:
    # Личный кабинет
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода
    ACCOUNT_INFO = (By.XPATH, "//a[text()='Профиль']")  # Заголовок профиля (для проверки входа)