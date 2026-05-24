#pytest -n 2 #for running parallelly
#pytest -m smoke #to run smoke tests only
#pytest run all tests
#pytest -m smoke --browser_name chrome --html=reports/report.html


import json
import os.path
import sys
from time import sleep

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObjects.login import LoginPage
from pageObjects.ShopPage import ShopPage

test_data_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "test_e2eframework.json",
)

with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2eframework(browserInstance,test_list_item):

    driver=browserInstance
    login=LoginPage(driver)

    print(login.getTitle())

    login.login(test_list_item["userEmail"],test_list_item["password"])

    # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()  # here *means contains

    # //div[@class='card h-100']/div/h4/a
    # product=//div[@class='card h-100']

    shop = ShopPage(driver)
    print(shop.getTitle())
    shop.add_products_to_cart(test_list_item["productName"])
    checkout_confirmation=shop.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("India")
    checkout_confirmation.validate_order()

    sleep(2)

