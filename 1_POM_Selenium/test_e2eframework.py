import os.path
import sys

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObjects.login import LoginPage

def test_e2eframework(browserInstance):

    driver=browserInstance

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    login=LoginPage(driver)
    login.login()


    # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()  # here *means contains

    # //div[@class='card h-100']/div/h4/a
    # product=//div[@class='card h-100']

    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for product in products:
        product_name = product.find_element(By.XPATH, "div/h4/a").text
        if product.text == 'Blackberry':
            product.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

    driver.find_element(By.CSS_SELECTOR, "#country").send_keys("India")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".suggestions")))
    driver.find_element(By.CSS_SELECTOR, ".suggestions").click()

    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    sleep(2)


