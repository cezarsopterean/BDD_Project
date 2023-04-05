from browser import Browser

class Base_page(Browser):

    def check_url(self, expected_url):
        actual_url = self.chrome.current_url
        assert actual_url == expected_url, f'Current url: {actual_url}, expected: {expected_url}'

    def correct_email(self, by, selector):
        self.chrome.find_element(by, selector).send_keys('kicewi8294@oniecan.com')

    def check_error_message(self, by, selector, expected_error_message):
        actual_error_message = self.chrome.find_element(by, selector).text
        assert actual_error_message == expected_error_message, f'Error, incorrect error message, actual: {actual_error_message}; expected: {expected_error_message}'

    def insert_keyword(self, by, selector, keyword):
        self.chrome.find_element(by, selector).send_keys(keyword)

    def check_keyword(self, by, selector, keyword):
        assert keyword in self.chrome.find_element(by, selector).text, 'Error: Keyword does not show up'