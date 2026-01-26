from selenium import webdriver
from time import sleep
from Pages.LoginPage import LoginPage

driver = webdriver.Chrome()
driver.get("https://www.actitime.com/free-online-trial")
sleep(5)
login = LoginPage(driver)
login.login("admin", "admin123",email="sandeep123@gmail.com")

sleep(5)
driver.quit()