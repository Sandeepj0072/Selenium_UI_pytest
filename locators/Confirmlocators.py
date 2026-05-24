from selenium.webdriver.common.by import By




class Confirmlocators:

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")
    COUNTRY_INPUT = (By.CSS_SELECTOR, "#country")
    COUNTRY_OPTION = (By.CSS_SELECTOR, ".suggestions")
    CHECKBOX = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    SUCCESS_MSG = (By.CLASS_NAME, "alert-success")

    @staticmethod
    def country_option(country_name):
        return (

            By.XPATH,

            f"//a[text()='{country_name}']"

        )



