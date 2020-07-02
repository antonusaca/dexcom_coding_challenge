from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def header(self):
        return self.wait.until(ec.visibility_of_any_elements_located(
            (By.XPATH, "//*[contains(text(),'Welcome to Dexcom CLARITY, your')]")))

    def open(self):
        self.driver.get("https://clarity.dexcom.com/")

    def check(self):
        return len(self.header) == 1
