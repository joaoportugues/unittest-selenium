from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "loginButton")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located(self.username))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

