Feature: Check if the inputted keywords and filters work on the search bars on each section

  Background:
    Given Search Page: I am on the search page

  @T1
    Scenario: Check that the keywords work on "ALL ITEMS"
    When Search Page: I click "ALL ITEMS"
    When Search Page: I input "paper"
    Then Search Page: I get the keyword "paper" and close it

  @T2
    Scenario: Check that the keywords work on "MY ITEMS"
    When Search Page: I click "MY ITEMS"
    When Search Page: I input "pen"
    Then Search Page: I get the keyword "pen" and close it

  @T3 @filterButton
    Scenario: Check if the filter button filters and takes inputs
    When Search Page: I click the filter button
    When Search Page: I click the "Type" button
    When Search Page: I select "Airplane"
    Then Search Page: I get the keyword "Airplane" and close it