from behave import *

@given('Search Page: I am on the search page')
def step_impl(context):
    context.search_page_object.navigate_search_page()

@then('Search Page: I can login and see the Search page')
def step_impl(context):
    context.search_page_object.check_login_success()

@when('Search Page: I click the dropdown menu')
def step_impl(context):
    context.search_page_object.click_dropdown()

@when('Search Page: I click logout')
def step_impl(context):
    context.search_page_object.click_logout()

@when('Search Page: I confirm the logout')
def step_impl(context):
    context.search_page_object.click_confirm_logout()

@when('Search Page: I click the Library button')
def step_impl(context):
    context.search_page_object.click_library()

@then('Search Page: I am taken to the Library page')
def step_impl(context):
    context.search_page_object.check_library_button()

@when('Search Page: I click the People button')
def step_impl(context):
    context.search_page_object.click_people()

@then('Search Page: I am taken to the People page')
def step_impl(context):
    context.search_page_object.check_people_button()

@when('Search Page: I click the Connections button')
def step_impl(context):
    context.search_page_object.click_connections()

@then('Search Page: I am taken to the Connections page')
def step_impl(context):
    context.search_page_object.check_connections_button()

@when('Search Page: I click the Add button')
def step_impl(context):
    context.search_page_object.click_add()

@then('Search Page: I am taken to the Add page')
def step_impl(context):
    context.search_page_object.check_add_button()