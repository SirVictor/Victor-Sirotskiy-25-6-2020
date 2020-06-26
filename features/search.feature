Feature: Herolo

#  Scenario: Check page title
#    Given I navigate to the Herolo page
#    Then I expect page title to equal "הירולו - חברת פיתוח מובילה המתמחה בפתרונות פרונט אנד"

  Scenario Outline: Check page title
    Given I navigate to the Herolo page
    Then I fill the form fields "<name>", "<company>", "<email>" and "<phone>"
    And I expect to be redirected to the thank you page: "<flag>"

    Examples:
    |  name  | company |       email         |    phone    | flag  |
    | victor |  home   | victorius@gmail.com | 0505820546  | True  |
    | victor |  null   | victorius@gmail.com | 0505820546  | False |
    |  null  |  null   |      null           | 0505820546  | False |
    | victor |  home   |      gmail.com      | 0505820546  | False |
    | victor |  work1  | victorius@gmail.com | 050-5820546 | True  |

#    Given I navigate to the PyPi Home page "<start>" "<eat>" lalala "<left>"
#    When I search for "behave"
#    Then I am taken to the PyPi Search Results page
#    And I see a search result "behave 1.2.5"

#  Scenario Outline: Search PyPI
#    Given I navigate to the Herolo page
#    And I expect page title to equal "הירולו - חברת פיתוח מובילה המתמחה בפתרונות פרונט אנד"
#
#    Examples:
#    | start | eat | left |
#    |  12   |  5  |  7   |
#    |  24   |  45 |  1   |