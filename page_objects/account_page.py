from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def username_field(self):
        return self.wait.until(ec.element_to_be_clickable((By.ID, "username")))

    @property
    def password_field(self):
        return self.wait.until(ec.element_to_be_clickable((By.ID, "password")))

    @property
    def login_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.ID, "edit-actions")))

    @property
    def credentials(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//*[text()='Nile PATest001']")))

    @property
    def unrecognized_credentials(self):
        return self.wait.until(
            ec.visibility_of_any_elements_located((By.XPATH, "//*[text()='Unrecognized username or password. ']")))

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()

    def check_positive(self):
        return len(self.credentials) == 1

    def check_negative(self):
        return len(self.unrecognized_credentials) == 1
