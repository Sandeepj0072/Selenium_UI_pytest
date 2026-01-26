from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
sleep(10)
company=['TCS','WIPRO','MARUTI']

for compan in company:
    print(f"{compan:>15}")


while   True:
    for compan in company:
        share_price=driver.find_element(By.XPATH,f"//a[text()='{compan}']/../..//td[7]").text
        print(share_price)
    print()
    sleep(5)

#
#
#
# current_title=driver.title
# print(current_title)
# current_url=driver.current_url
# print(current_url)
# sleep(2)
# textbox=driver.find_element(By.XPATH,"//a[text()='Register']")
# textbox.click()
# sleep(2)
# select_geneder=driver.find_element(By.XPATH,"//input[@name='Gender'][1]")
# select_geneder.click()
# sleep(10)
