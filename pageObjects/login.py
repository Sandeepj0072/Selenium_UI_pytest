from selenium.webdriver.common.by import By
from utils.browserutils import BrowserUtils
from locators.LoginLocators import LoginLocators



class LoginPage(BrowserUtils):


    def __init__(self, driver):

        super().__init__(driver) #here we are initializing parent class coinstructor to driver so that our utils will get driver

    def login(self,username,password):

        self.type(LoginLocators.USERNAME_INPUT,username)
        self.type(LoginLocators.PASSWORD_INPUT,password) #You don’t see find_element, but it is still happening internally.
        self.click(LoginLocators.SIGN_BUTTON)
