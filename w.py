from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print(driver.title)
print(driver.current_url)

sleep(3)

# 🔹 Check if iframe exists
iframes = driver.find_elements(By.TAG_NAME, "iframe")
print("Total iframes found:", len(iframes))

if len(iframes) > 0:
    driver.switch_to.frame(iframes[0])
    sleep(2)

    try:
        agree = driver.find_element(
            By.XPATH, "//button//div[text()='Accept all' or text()='I agree']"
        )
        agree.click()
    except:
        pass

    driver.switch_to.default_content()
    sleep(2)

# 🔹 Now locate search box (works when iframe = 0 or >0)
textbox = driver.find_element(By.NAME, "q")
textbox.click()
textbox.send_keys("Selenium basics")

sleep(5)
driver.quit()