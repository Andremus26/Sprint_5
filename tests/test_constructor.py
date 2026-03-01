from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators

class TestConstructor:
    def test_switch_to_buns(self, driver):
        # Нажимаем на вкладку "Соусы", чтобы активной стала не "Булки"
        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)
        ).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text

    def test_switch_to_sauces(self, driver):
        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text

    def test_switch_to_fillings(self, driver):
        driver.find_element(*MainPageLocators.FILLINGS_TAB).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "Начинки" in active_tab.text