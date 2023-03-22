from behave import *

@then('PassReset Page: I am taken to the password reset page')
def step_impl(context):
    context.passreset_page_object.forgotPass_link()

@when('PassReset Page: I enter the email "kicewi8294@oniecan.com"')
def step_impl(context):
    context.passreset_page_object.insert_correct_email()

@when('PassReset Page: I click the send email button')
def step_impl(context):
    context.passreset_page_object.click_send_email()

@then('PassReset Page: I get the reset email send confirmation')
def step_impl(context):
    context.passreset_page_object.confirmation()