import pytest
from selenium import webdriver
import time
from page_objects.landing_page import LandingPage
from page_objects.home_user_page import HomeUserPage
from page_objects.account_page import AccountPage
from webdriver_manager.chrome import ChromeDriverManager


class TestLoginFeature:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())

        yield
        time.sleep(5)
        driver.quit()

    def test_open_title_page(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        assert landing_page.check()

    def test_open_account_page(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        home_user_page = HomeUserPage(driver)
        home_user_page.open_home_user_page()
        assert home_user_page.check()

    def test_login_positive(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        home_user_page = HomeUserPage(driver)
        home_user_page.open_home_user_page()
        account_page = AccountPage(driver)
        account_page.login(username="nilepatest001", password="Password@1")
        assert account_page.check_positive()

    def test_login_negative(self, test_setup):
        landing_page = LandingPage(driver)
        landing_page.open()
        home_user_page = HomeUserPage(driver)
        home_user_page.open_home_user_page()
        account_page = AccountPage(driver)
        account_page.login(username="nilepatest001", password="Password@")
        assert account_page.check_negative()
