from browser import Browser
from pages.login_page import Login_page
from pages.search_page import Search_page
from pages.passreset_page import PassReset_page

def before_all(context):
    context.browser = Browser
    context.login_page_object = Login_page()
    context.search_page_object = Search_page()
    context.passreset_page_object = PassReset_page()

def after_all(context):
    context.browser.close()