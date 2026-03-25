
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.browserutils import BrowserUtils


class Checkout_Confirmation(BrowserUtils):

    def __init__(self,driver):

        super().__init__(driver)  # here we are initializing parent class coinstructor to driver so that our utils will get driver

        self.driver=driver
        self.CHECKOUT_BUTTON=(By.CSS_SELECTOR, ".btn.btn-success")
        self.COUNTRY_INPUT=(By.CSS_SELECTOR, "#country")
        self.COUNTRY_OPTION=(By.CSS_SELECTOR, ".suggestions")
        self.CHECKBOX=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.SUBMIT_BUTTON=(By.CSS_SELECTOR, "input[type='submit']")
        self.SUCCESS_MSG=(By.CLASS_NAME,"alert-success")



    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)


    def enter_delivery_address(self,country_name):

        self.driver.find_element(*self.COUNTRY_INPUT).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.COUNTRY_OPTION))
        self.driver.find_element(*self.COUNTRY_OPTION).click()
        self.driver.find_element(*self.CHECKBOX).click()
        self.driver.find_element(*self.SUBMIT_BUTTON).click()


    def validate_order(self):
        successText=self.driver.find_element(*self.SUCCESS_MSG).text
        assert "Success! Thank you!" in successText

