from behave import *

@given('Login Page: I am on the Jules.app login page')
def step_impl(context):
    context.login_page_object.navigate_login_page()

@when('Login Page: I insert the email "kicewi8294@oniecan.com" and the password "Testpassword_1"')
def step_impl(context):
    context.login_page_object.insert_correct_email()
    context.login_page_object.correct_pass()

@when('Login Page: I click the login button')
def step_impl(context):
    context.login_page_object.click_login()

@then('Login Page: I am taken to the login page')
def step_impl(context):
    context.login_page_object.check_logout_success()

@when('Login Page: I insert the email "{email}" and the password "{password}"')
def step_impl(context, email, password):
    context.login_page_object.insert_email(email)
    context.login_page_object.insert_pass(password)

@then('Login Page: I cannot login and receive the error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page_object.error_check(error_message)

@then('Login Page: The loging button is disabled')
def step_impl(context):
    context.login_page_object.login_button_check()

@when('Login Page: I insert the email "kicewi8294@oniecan.com"')
def step_impl(context):
    context.login_page_object.insert_correct_email()

@when('Login Page: I insert the password "Testpassword_1"')
def step_impl(context):
    context.login_page_object.correct_pass()

@when('Login Page: I click the "Forgot password?" link')
def step_impl(context):
    context.login_page_object.click_forgotPassword()

@then('Login Page: Login')
def step_impl(context):
    context.login_page_object.insert_correct_email()
    context.login_page_object.correct_pass()
    context.login_page_object.click_login()