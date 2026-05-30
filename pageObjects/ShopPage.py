
from selenium.webdriver.common.by import By
from pageObjects.Checkout_confirmation import Checkout_Confirmation
from utils.browserutils import BrowserUtils
from locators.ShoppageLocators import ShoppageLocators

class ShopPage(BrowserUtils):

    def __init__(self,driver):

        super().__init__(driver)

    def add_products_to_cart(self,product_name):

        products = self.find_elements(ShoppageLocators.PRODUCT_CARDS)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()


    def goToCart(self):

        self.click(ShoppageLocators.CHECKOUT_BUTTON)
        checkout_confirmation=Checkout_Confirmation(self.driver)
        return checkout_confirmation

