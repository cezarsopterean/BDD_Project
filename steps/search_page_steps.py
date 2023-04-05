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

@when('Search Page: I click on the question mark button')
def step_impl(context):
    context.search_page_object.click_2nd_dropdown()

@then('Search Page: I check if the FAQ button is visible')
def step_impl(context):
    context.search_page_object.check_FAQ()

@when ('Search Page: I click "ALL ITEMS"')
def step_impl(context):
    context.search_page_object.click_all_items()

@when ('Search Page: I input "paper"')
def step_impl(context):
    context.search_page_object.insert_keyword1()

@then ('Search Page: I get the keyword "paper" and close it')
def step_impl(context):
    context.search_page_object.check_keyword1()
    context.search_page_object.close_keyword()

@when ('Search Page: I click "MY ITEMS"')
def step_impl(context):
    context.search_page_object.click_my_items()

@when ('Search Page: I input "pen"')
def step_impl(context):
    context.search_page_object.insert_keyword2()

@then ('Search Page: I get the keyword "pen" and close it')
def step_impl(context):
    context.search_page_object.check_keyword2()
    context.search_page_object.close_keyword()

@when ('Search Page: I click the filter button')
def step_impl(context):
    context.search_page_object.click_filter_button()

@when ('Search Page: I click the "Type" button')
def step_impl(context):
    context.search_page_object.click_type_filter_button()

@when ('Search Page: I select "Airplane"')
def step_impl(context):
    context.search_page_object.click_filter_button_airplane()

@then ('Search Page: I get the keyword "Airplane" and close it')
def step_impl(context):
    context.search_page_object.check_filter_keyword()
    context.search_page_object.close_filter_keyword()