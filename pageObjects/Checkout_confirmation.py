
from utils.browserutils import BrowserUtils
from locators.Confirmlocators import Confirmlocators




class Checkout_Confirmation(BrowserUtils):

    def __init__(self,driver):

        super().__init__(driver)  # here we are initializing parent class coinstructor to driver so that our utils will get driver

        self.driver=driver


    def checkout(self):
        self.click(Confirmlocators.CHECKOUT_BUTTON)


    def enter_delivery_address(self,country_name):

        # self.driver.find_element(*self.COUNTRY_INPUT).send_keys(country_name)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located(self.COUNTRY_OPTION))
        #

        # self.driver.find_element(*self.COUNTRY_OPTION).click()

        #USING BROWSER UTILS UTILITY EASY MODULE
        self.type(Confirmlocators.COUNTRY_INPUT,country_name)

        #self.click(Confirmlocators.COUNTRY_OPTION)

        self.click(Confirmlocators.country_option(country_name))



        checkbox = self.find_element(Confirmlocators.CHECKBOX)

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",checkbox)

        self.driver.execute_script("arguments[0].click();",checkbox)

        self.click(Confirmlocators.SUBMIT_BUTTON)


    def validate_order(self):
        successText=self.get_text(Confirmlocators.SUCCESS_MSG)
        assert "Success! Thank you!" in successText

