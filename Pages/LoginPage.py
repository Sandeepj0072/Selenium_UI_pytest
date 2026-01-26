
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.locators import *

glpat-li74qHdfFR6qgaU_ApLA2mM6MQpvOjEKdTpqb2praA8.01.171cb2y2y

class LoginPage:
     def __init__(self,driver):
         self.driver=driver

     def enter_username(self,username):
         self.driver.find_element(*USERNAME_INPUT).send_keys(username)

     def last_name(self,lastname):
         self.driver.find_element(*LAST_NAME_INPUT).send_keys(lastname)

     def email_input(self,email):
         self.driver.find_element(*EMAIL_INPUT).send_keys(email)

     def click_confirm(self):
         sleep(5)
         self.driver.find_element(*CONFIRM_INPUT).click()

     def login(self,username,lastname,email):

         self.enter_username(username)
         self.last_name(lastname)
         self.email_input(email)

         self.click_confirm()

