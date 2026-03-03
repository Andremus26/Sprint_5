import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators

class TestConstructor:
    @pytest.mark.parametrize(
        "tab_locator, expected_text",
        [
            (MainPageLocators.BUNS_TAB, "Булки"),
            (MainPageLocators.SAUCES_TAB, "Соусы"),
            (MainPageLocators.FILLINGS_TAB, "Начинки"),
        ]
    )
    def test_switch_to_tab(self, driver, tab_locator, expected_text):
        # Предварительно кликаем на булки, чтобы активной была какая-то вкладка
        driver.find_element(*MainPageLocators.BUNS_TAB).click()
        # Кликаем на проверяемую вкладку
        driver.find_element(*tab_locator).click()
        # Ждём, пока активная вкладка станет видимой и проверим текст
        active_tab = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB)
        )
        assert expected_text in active_tab.text