

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_sort(browserInstance):
    driver=browserInstance
    browserSortedVeggies=[]

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    driver.find_element(By.XPATH,"//span[contains(text(),'Veg/fruit name')]").click()

    veggieWebElements=driver.find_elements(By.XPATH,"//tr/td[1]")
    for element in veggieWebElements:
        # print(element)
        browserSortedVeggies.append(element.text)

    originalBroswerSortedList=browserSortedVeggies.copy()

    browserSortedVeggies.sort()
    assert browserSortedVeggies == originalBroswerSortedList

