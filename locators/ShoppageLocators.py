from selenium.webdriver.common.by import By




class ShoppageLocators:

    PRODUCT_CARDS = (By.XPATH, "//div[@class='card h-100']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")


