
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)


# Dropdown Selectors

driver.find_element(By.NAME,"email").send_keys("jasjsj")
dropdown=Select(driver.find_element(By.CSS_SELECTOR,"select[class='form-control']"))
sleep(1)
dropdown.select_by_visible_text("Female")
sleep(1)

checkboxs=driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in checkboxs:
    print(checkbox.get_attribute("value"))


# Green Kart -- Web driver waiting

buttons=driver.find_elements(By.XPATH,"//div[@class='products']/div")
for button in buttons:
    button.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("fsdf")
driver.find_element(By.CSS_SELECTOR,".PromoBtn").click()


wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
# s=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
s=driver.find_element(By.CSS_SELECTOR,".promoInfo").get_attribute("value")

print(s)



# mouse actions with PP practice page

action=ActionChains(driver)

action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
sleep(3)
action.context_click(driver.find_element(By.PARTIAL_LINK_TEXT,"Top")).perform()
sleep(10)