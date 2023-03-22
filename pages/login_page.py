from selenium.webdriver.common.by import By
from base_page import Base_page

class Login_page(Base_page):
    EMAIL = (By.XPATH, '//input[@type="text"]')
    PASSWORD = (By.XPATH, '//input[@type="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@id="client-snackbar"]/div/span')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[@data-test-id="forgot-password-link"]')

    def navigate_login_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def insert_correct_email(self):
        self.correct_email(*self.EMAIL)

    def correct_pass(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('Testpassword_1')

    def insert_email(self, email):
        self.chrome.find_element(*self.EMAIL).send_keys(email)

    def insert_pass(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def check_logout_success(self):
        self.check_url('https://jules.app/sign-in')

    def error_check(self, expected_error_message):
        self.check_error_message(*self.ERROR_MESSAGE, expected_error_message)

    def login_button_check(self):
        loginButton = self.chrome.find_element(*self.LOGIN_BUTTON)
        assert loginButton.is_enabled() == False, f'Error, the login button is displayed when it should not be'

    def click_forgotPassword(self):
        self.chrome.find_element(*self.FORGOT_PASSWORD_BUTTON).click()