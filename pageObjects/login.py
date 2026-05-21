from selenium.webdriver.common.by import By
from utils.browserutils import BrowserUtils




class LoginPage(BrowserUtils):


    def __init__(self, driver):

        super().__init__(driver) #here we are initializing parent class coinstructor to driver so that our utils will get driver

        self.driver=driver #this driver is avaialble,the moment you attach this piece here you can use it anywhere
        self.USERNAME_INPUT=(By.ID, "username")
        self.PASSWORD_INPUT=(By.NAME, "password")#with self keyword the scope of locator is accessed outside and wont die within
        self.SIGN_BUTTON=(By.ID, "signInBtn")


    def login(self,username,password):

        self.type(self.USERNAME_INPUT,username)
        self.type(self.PASSWORD_INPUT,password) #You don’t see find_element, but it is still happening internally.
        self.click(self.SIGN_BUTTON)
