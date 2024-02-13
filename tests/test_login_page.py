import unittest
from base_test import BaseTest
from pages.login_page import LoginPage

class TestLoginPage(BaseTest):
    def test_successful_login(self):
        self.driver.get("https://example.com/login")
        login_page = LoginPage(self.driver)
        login_page.enter_username("your_username")
        login_page.enter_password("your_password")
        login_page.click_login_button()
        self.assertIn("Dashboard", self.driver.title)

if __name__ == "__main__":
    unittest.main()

