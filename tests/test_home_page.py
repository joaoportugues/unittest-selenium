import unittest
from base_test import BaseTest
from pages.home_page import HomePage

class TestHomePage(BaseTest):
    def test_home_page_title(self):
        self.driver.get("https://example.com")
        home_page = HomePage(self.driver)
        self.assertIn("Home Page", home_page.get_title())

if __name__ == "__main__":
    unittest.main()

