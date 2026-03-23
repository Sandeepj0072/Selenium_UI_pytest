import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name=="firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
    yield driver
    driver.close() #post your test execution
