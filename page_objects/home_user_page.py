from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class HomeUserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def header(self):
        return self.wait.until(
            ec.visibility_of_any_elements_located((By.XPATH, "//*[text()='Sign in to manage your account.']")))

    @property
    def home_user(self):
        return self.driver.find_element_by_xpath("//*[text()='Dexcom CLARITY for Home Users']")

    def open_home_user_page(self):
        self.home_user.click()
        return HomeUserPage(self.driver)

    def check(self):
        return len(self.header) == 1
