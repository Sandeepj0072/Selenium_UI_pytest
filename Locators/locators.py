from selenium.webdriver.common.by import By

# Login Page Locators
USERNAME_INPUT = (By.XPATH, "//input[@placeholder='First Name *']")
LAST_NAME_INPUT=(By.ID, "LastName")
EMAIL_INPUT=(By.ID, "Email")

CONFIRM_INPUT =(By.ID, "confirm-button")

PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
LOGIN_BUTTON   = (By.XPATH, "//button[@type='submit']")

# Home Page Locators (example)
PROFILE_ICON = (By.XPATH, "//div[@id='profile']")
LOGOUT_BTN   = (By.XPATH, "//a[text()='Logout']")


