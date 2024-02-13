from selenium.webdriver.common.by import By

class LoginPage:
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "loginButton")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.username)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

