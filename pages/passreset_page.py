from selenium.webdriver.common.by import By
from base_page import Base_page

class PassReset_page(Base_page):
    EMAIL = (By.XPATH, '//input[@placeholder="Enter your email"]')
    SEND_EMAIL_BUTTON = (By.XPATH, '//button[@data-test-id="login-button"]')
    EMAIL_SEND_CONFIRMATION = (By.XPATH, '//*[@id="client-snackbar"]/div/div/span')

    def forgotPass_link(self):
        self.check_url('https://jules.app/forgot-password')

    def insert_correct_email(self):
        self.correct_email(*self.EMAIL)

    def click_send_email(self):
        self.chrome.find_element(*self.SEND_EMAIL_BUTTON).click()

    def confirmation(self):
        message = self.chrome.find_element(*self.EMAIL_SEND_CONFIRMATION).text
        assert 'Email Sent' in message, f'Error: Confirmation message does not appear'