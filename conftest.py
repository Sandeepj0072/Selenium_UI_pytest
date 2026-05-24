import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

        options = Options()
        prefs = {

            "credentials_enable_service": False,

            "profile.password_manager_enabled": False,

            "profile.default_content_setting_values.notifications": 2,

        }

        options.add_experimental_option("prefs", prefs)

        # Extra strong disable flags

        options.add_argument("--disable-notifications")

        options.add_argument("--disable-save-password-bubble")

        options.add_argument("--disable-infobars")

        # 🔥 IMPORTANT: disable password manager features

        options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordManagerEnableAutoSignin")

        # Use fresh profile (VERY important)

        options.add_argument("--incognito")

        options.add_argument("--no-first-run")

        options.add_argument("--no-default-browser-check")
        if os.getenv("CI"):

            options.add_argument("--headless=new")
        options.add_argument("--headless=new")

        options.add_argument("--disable-dev-shm-usage")

        options.add_argument("--window-size=1920,1080")

        options.add_argument("--disable-gpu")

        options.add_argument("--no-sandbox")

        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.quit()
