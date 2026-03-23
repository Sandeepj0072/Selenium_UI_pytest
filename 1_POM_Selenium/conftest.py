import pytest

from selenium import webdriver

@pytest.fixture(scope="function")
def browserInstance():
    driver = webdriver.Chrome()
    if browser_name == "chrome":

        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.implicitly_wait(5)
    yield driver