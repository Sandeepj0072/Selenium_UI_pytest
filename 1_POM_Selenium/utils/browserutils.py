from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains


class BrowserUtils:

    def __init__(self,driver):
        self.driver=driver

    # -------- Element Actions --------


    def click(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).text


    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(locator))

        # Here you explicitly call: find_element then .click()



    # -------- Browser Utils --------
    def getTitle(self):
        return self.driver.title

        # -------------------------

        # 🔽 SELECT UTILITIES

        # -------------------------

    def select_by_visible_text(self, locator, text):
        element = self.driver.find_element(*locator)

        Select(element).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        element = self.driver.find_element(*locator)

        Select(element).select_by_value(value)

    def select_by_index(self, locator, index):
        element = self.driver.find_element(*locator)

        Select(element).select_by_index(index)

        # -------------------------

        # 🖱 ACTION UTILITIES

        # -------------------------

    def hover(self, locator):
        element = self.driver.find_element(*locator)

        ActionChains(self.driver).move_to_element(element).perform()

    def right_click(self, locator):
        element = self.driver.find_element(*locator)

        ActionChains(self.driver).context_click(element).perform()

    def double_click(self, locator):
        element = self.driver.find_element(*locator)

        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)

        target = self.driver.find_element(*target_locator)

        ActionChains(self.driver).drag_and_drop(source, target).perform()







