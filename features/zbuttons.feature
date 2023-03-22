Feature: Check if the buttons and dropdown menus work correctly

  Background:
    Given Search Page: I am on the search page

  @T1 @navigationButtons
    Scenario: Check if the buttons send you to the correct page
    Then Login Page: Login
    When Search Page: I click the Library button
    Then Search Page: I am taken to the Library page
    When Search Page: I click the People button
    Then Search Page: I am taken to the People page
    When Search Page: I click the Connections button
    Then Search Page: I am taken to the Connections page
    When Search Page: I click the Add button
    Then Search Page: I am taken to the Add page