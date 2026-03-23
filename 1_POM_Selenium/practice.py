
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from Pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)


driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click() #here *means contains

#//div[@class='card h-100']/div/h4/a
# product=//div[@class='card h-100']

products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    product_name=product.find_element(By.XPATH,"div/h4/a").text
    if product.text=='Blackberry':
        product.find_element(By.XPATH,"div/button").click()


driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']").click()

driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()


driver.find_element(By.CSS_SELECTOR,"#country").send_keys("India")
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".suggestions")))
driver.find_element(By.CSS_SELECTOR,".suggestions").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()


driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
sleep(10)


