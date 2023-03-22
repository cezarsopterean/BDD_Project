from selenium.webdriver.common.by import By
from base_page import Base_page
from time import sleep

class Search_page(Base_page):
    LOGIN_PAGE_MESSAGE = (By.CLASS_NAME, 'css-1h5x3dy')
    DROPDOWN = (By.XPATH, '//div[@class="css-1qkwfbr"]/div[3]')
    LOGOUT_BUTTON = (By.XPATH, '//div[@data-test-id="logout-option-business"]')
    LOGOUT_CONFIRM_BUTTON = (By.XPATH, '//button[@data-test-id="confirm-logout-button"]')
    LIBRARY_BUTTON = (By.XPATH, '//div[@data-test-id="library-navigation-button"]')
    PEOPLE_BUTTON = (By.XPATH, '//div[@data-test-id="people-navigation-button"]')
    CONNECTIONS_BUTTON = (By.XPATH, '//div[@data-test-id="connections-navigation-button"]')
    ADD_BUTTON = (By.XPATH, '//div[@data-test-id="add-flows-navigation-button"]')

    def check_login_success(self):
        sleep(2)
        self.check_url('https://jules.app/search/all')

    def click_dropdown(self):
        self.chrome.find_element(*self.DROPDOWN).click()

    def click_logout(self):
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()

    def click_confirm_logout(self):
        self.chrome.find_element(*self.LOGOUT_CONFIRM_BUTTON).click()

    def navigate_search_page(self):
        self.chrome.get('https://jules.app/search/all')

    def click_library(self):
        self.chrome.find_element(*self.LIBRARY_BUTTON).click()

    def check_library_button(self):
        self.check_url('https://jules.app/library/records')

    def click_people(self):
        self.chrome.find_element(*self.PEOPLE_BUTTON).click()

    def check_people_button(self):
        self.check_url('https://jules.app/people')

    def click_connections(self):
        self.chrome.find_element(*self.CONNECTIONS_BUTTON).click()

    def check_connections_button(self):
            self.check_url('https://jules.app/connections')

    def click_add(self):
        self.chrome.find_element(*self.ADD_BUTTON).click()

    def check_add_button(self):
        self.check_url('https://jules.app/add')