from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class LoginPage:


    def __init__(self, driver):
        self.driver=driver #this driver is avaialble,the moment you attach this piece here you can use it anywhere
        self.USERNAME_INPUT=(By.ID, "username")
        self.PASSWORD_INPUT=(By.NAME, "password")#with self keyword the scope of locator is accessed outside and wont die within
        self.SIGN_BUTTON=(By.ID, "signInBtn")


    def login(self):

        self.driver.find_element(*self.USERNAME_INPUT).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.SIGN_BUTTON).click()
