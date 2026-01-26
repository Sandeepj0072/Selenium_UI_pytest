from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options
options = Options()
options.add_argument("--start-maximized")

# Setup WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://meetings.asco.org/meetings")
time.sleep(8)  # wait for Flutter page to load

# Get viewport size
viewport_width = driver.execute_script("return window.innerWidth")
viewport_height = driver.execute_script("return window.innerHeight")
print("Viewport size:", viewport_width, viewport_height)

# Grid-based clicks
step_x = 100  # horizontal step
step_y = 100  # vertical step

# Loop through page
for y in range(100, viewport_height, step_y):
    for x in range(100, viewport_width, step_x):
        try:
            actions = ActionChains(driver)
            actions.move_by_offset(x, y).click().perform()
            time.sleep(1)  # wait for any UI changes

            # Optional: take a screenshot after each click
            driver.save_screenshot(f"screenshot_{x}_{y}.png")
            print(f"Clicked at ({x},{y})")

            # Reset mouse position to avoid offset compounding
            actions.move_to_element(driver.find_element("tag name", "body")).perform()
        except Exception as e:
            print(f"Could not click at ({x},{y}): {e}")

# Close browser
driver.quit()