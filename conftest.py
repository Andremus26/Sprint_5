import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    # Настройка Chrome для запуска тестов
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    # При необходимости можно добавить headless режим:
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()