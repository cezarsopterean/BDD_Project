from selenium.webdriver.common.by import By
from base_page import Base_page
from time import sleep
from selenium.webdriver.common.keys import Keys

class Search_page(Base_page):
    LOGIN_PAGE_MESSAGE = (By.CLASS_NAME, 'css-1h5x3dy')
    DROPDOWN = (By.XPATH, '//div[@class="css-1qkwfbr"]/div[3]')
    LOGOUT_BUTTON = (By.XPATH, '//div[@data-test-id="logout-option-business"]')
    LOGOUT_CONFIRM_BUTTON = (By.XPATH, '//button[@data-test-id="confirm-logout-button"]')
    LIBRARY_BUTTON = (By.XPATH, '//div[@data-test-id="library-navigation-button"]')
    PEOPLE_BUTTON = (By.XPATH, '//div[@data-test-id="people-navigation-button"]')
    CONNECTIONS_BUTTON = (By.XPATH, '//div[@data-test-id="connections-navigation-button"]')
    ADD_BUTTON = (By.XPATH, '//div[@data-test-id="add-flows-navigation-button"]')
    QUESTION_MARK_BUTTON = (By.CSS_SELECTOR, 'div.css-1qkwfbr>div:nth-of-type(2)')
    FAQ_BUTTON = (By.CSS_SELECTOR, '.MuiPaper-root.jss6>ul>a:first-of-type>div:first-of-type')
    ALL_ITEMS_BUTTON = (By.CSS_SELECTOR, '.MuiTabs-flexContainer>button:first-of-type')
    MY_ITEMS_BUTTON = (By.CSS_SELECTOR, '.MuiTabs-flexContainer>button:nth-of-type(2)')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.MuiInputBase-root>input')
    KEYWORD = (By.CSS_SELECTOR, '.css-1a4a8xn>div:nth-of-type(2)>div:nth-of-type(2)>div>div>div>div')
    KEYWORD_X = (By.CSS_SELECTOR, '.css-1a4a8xn>div:nth-of-type(2)>div:nth-of-type(2)>div>div>div:nth-of-type(2)>button')
    FILTER_BUTTON = (By.CSS_SELECTOR, '.css-1cnn1hc>div>div:nth-of-type(3)>div:nth-of-type(2)>div>div>button')
    FILTER_TYPE_BUTTON = (By.CSS_SELECTOR, '.jss7>div>ul>div:nth-of-type(2)')
    FILTER_AIRPLANE = (By.XPATH, '//div[text()="Airplane"]')
    FILTER_KEYWORD = (By.CSS_SELECTOR, '.css-1a4a8xn>div:nth-of-type(2)>div:nth-of-type(2)>div>div:first-of-type>div:nth-of-type(3)')
    FILTER_KEYWORD_CLOSE = (By.CSS_SELECTOR, '.css-1a4a8xn>div:nth-of-type(2)>div:nth-of-type(2)>div>div:first-of-type>div:nth-of-type(4)')

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

    def click_2nd_dropdown(self):
        self.chrome.find_element(*self.QUESTION_MARK_BUTTON).click()

    def check_FAQ(self):
        assert self.chrome.find_element(*self.FAQ_BUTTON).text == 'FAQ', 'Error: FAQ button is missing'

    def click_all_items(self):
        self.chrome.find_element(*self.ALL_ITEMS_BUTTON).click()

    def click_my_items(self):
        self.chrome.find_element(*self.MY_ITEMS_BUTTON).click()

    def insert_keyword1(self):
        self.insert_keyword(*self.SEARCH_FIELD, 'paper')
        self.chrome.find_element(*self.SEARCH_FIELD).send_keys(Keys.ENTER)

    def check_keyword1(self):
        self.check_keyword(*self.KEYWORD, 'paper')

    def insert_keyword2(self):
        self.insert_keyword(*self.SEARCH_FIELD, 'pen')
        self.chrome.find_element(*self.SEARCH_FIELD).send_keys(Keys.ENTER)

    def check_keyword2(self):
        self.check_keyword(*self.KEYWORD, 'pen')

    def close_keyword(self):
        self.chrome.find_element(*self.KEYWORD_X).click()

    def click_filter_button(self):
        self.chrome.find_element(*self.FILTER_BUTTON).click()

    def click_type_filter_button(self):
        self.chrome.find_element(*self.FILTER_TYPE_BUTTON).click()

    def click_filter_button_airplane(self):
        self.chrome.find_element(*self.FILTER_AIRPLANE).click()

    def check_filter_keyword(self):
        self.check_keyword(*self.FILTER_KEYWORD, 'Airplane')

    def close_filter_keyword(self):
        self.chrome.find_element(*self.FILTER_KEYWORD_CLOSE).click()