Feature: Herolo

  Scenario: Check page title
    Given I navigate to the Herolo page
    Then I expect page title to equal "הירולו - חברת פיתוח מובילה המתמחה בפתרונות פרונט אנד"


  Scenario Outline: Check Error Message with empty Field
    Given I navigate to the Herolo page
    Then I fill the form fields "<field_name>" with "" I expect to see error massage

    Examples:
      |   field_name   |
      |      name      |
      |     company    |
      |      email     |
      |    telephone   |

  Scenario Outline: Check Error Message with filled Field
    Given I navigate to the Herolo page
    Then I fill the form field "<name>" with "<text>" and "<flag>" of Case
    And I expect that in False "<flag>" case(wrong text for this field) will event error message and True case will not

    Examples:
    |   name  |  text               | flag  |
    |   name  | Victor              | True  |
    |   name  |  1234               | True  |
    |   name  |  vic12              | True  |
    | company | Victor              | True  |
    | company |  vic12              | True  |
    | company |  1234               | True  |
    |  email  |  victor@gmail.com   | True  |
    |  email  |  1234               | False |
    |  email  |  vic12              | False |
    |  email  |   @vc.com           | False |
    |  email  |  vic                | False |
    |  email  |  victor@gmail       | False |
    |  email  |  victor@gmail.      | False |
    |  email  | victorius@gmail.com | True  |
    |telephone|  victor             | False |
    |telephone|  1234               | False |
    |telephone|  vic126             | False |
    |telephone|  0505820546         | True  |
    |telephone|  0642222224         | False |
    |telephone|  1234567890         | False |
    |telephone|052466546646652456882| False |
    |telephone|  050582054          | False |
    |telephone|  039179222          | True  |
    |telephone|  03-9179222         | True  |
    |telephone|  050-5820546        | True  |


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