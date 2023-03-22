Feature: Check the functionality of the login page

  Background:
    Given Login Page: I am on the Jules.app login page

    @T1 @loginSuccessful
      Scenario: Check that you can login when providing correct credentials
      When Login Page: I insert the email "kicewi8294@oniecan.com" and the password "Testpassword_1"
      When Login Page: I click the login button
      Then Search Page: I can login and see the Search page

    @T2 @logout
      Scenario: Check that you can logout while logged in
      When Search Page: I click the dropdown menu
      When Search Page: I click logout
      When Search Page: I confirm the logout
      Then Login Page: I am taken to the login page

    @T3 @invalidLogin
      Scenario Outline: Check that you cannot login with invalid credentials
      When Login Page: I insert the email "<email>" and the password "<password>"
      When Login Page: I click the login button
      Then Login Page: I cannot login and receive the error message "<error_message>"

    @incorrectCredentials
      Examples:
      | email                     | password          | error_message                      |
      | fakemail@something.com    | Testpassword_1    | Invalid email/password combination |
      | kicewi8294@oniecan.com    | incorrect_pass    | Invalid email/password combination |
      | fakemail@something.com    | incorrect_pass    | Invalid email/password combination |

    @T4 @emptyFields
      Scenario: Check if the login button is displayed while both fields are empty
      Then Login Page: The loging button is disabled
      Scenario: Check if the login button is displayed while password field is empty
      When Login Page: I insert the email "kicewi8294@oniecan.com"
      Then Login Page: The loging button is disabled
      Scenario: Check if the login button is displayed while email field is empty
      When Login Page: I insert the password "Testpassword_1"
      Then Login Page: The loging button is disabled

    @T5 @passwordReset
      Scenario: Check if the reset password link works and the reset email is sent
      When Login Page: I click the "Forgot password?" link
      Then PassReset Page: I am taken to the password reset page
      When PassReset Page: I enter the email "kicewi8294@oniecan.com"
      When PassReset Page: I click the send email button
      Then PassReset Page: I get the reset email send confirmation
