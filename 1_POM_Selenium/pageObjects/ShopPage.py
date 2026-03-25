
from selenium.webdriver.common.by import By
from pageObjects.Checkout_confirmation import Checkout_Confirmation
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self,driver):

        super().__init__(driver)

        self.driver=driver
        self.PRODUCT_CARDS=(By.XPATH, "//div[@class='card h-100']")
        self.CHECKOUT_BUTTON=(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")


    def add_products_to_cart(self,product_name):

        products = self.driver.find_elements(*self.PRODUCT_CARDS)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()


    def goToCart(self):

        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        checkout_confirmation=Checkout_Confirmation(self.driver)
        return checkout_confirmation

