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


  Scenario Outline: Check page form
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


  Scenario Outline: Check social network Links
    Given I navigate to the Herolo page
    When I click on "<social>" link
    Then I expect for opening new window with Url "<url>"

  Examples:
  |  social   |                 url                              |
  | Facebook  | https://www.facebook.com/Herolofrontend          |
  | Linkedin  | https://www.linkedin.com/                        |
  | WhatsApp1 | https://api.whatsapp.com/send?phone=972544945333 |
  | WhatsApp2 | https://api.whatsapp.com/send?phone=972544945333 |
  | WebSite   | https://herolo.co.il/?lang=he                    |


  Scenario Outline: Check Scroll Link
  Given I navigate to the Herolo page
  Then I scroll "<down>" and wait 1 sec
  Then I search and after click on scroll button
  And I expect scroll from "<down>" to Top

  Examples:
  | down |
  | 5000 |
  | 3000 |
  | 2000 |
  | 1000 |



  Scenario: Check Valid Email Link
    Given I navigate to the Herolo page
    Then I search for a Mail link
    And I expect that link is valid (start with mailto:)


  Scenario Outline: Check Error Message with empty Field in FooterForm
    Given I navigate to the Herolo page
    Then I fill the footer form fields "<field_name>" with "" I expect to see error massage

    Examples:
      |   field_name   |
      |      name      |
      |      email     |
      |      phone     |


  Scenario Outline: Check Error Message with filled Field FooterForm
    Given I navigate to the Herolo page
    Then I fill the footer form field "<name>" with "<text>" and "<flag>" of Case
    And I expect that in False "<flag>" case(wrong text for this field) will event error message and True case will not

    Examples:
    |   name  |  text               | flag  |
    |   name  | Victor              | True  |
    |   name  |  1234               | True  |
    |   name  |  vic12              | True  |
    |  email  |  victor@gmail.com   | True  |
    |  email  |  1234               | False |
    |  email  |  vic12              | False |
    |  email  |   @vc.com           | False |
    |  email  |  vic                | False |
    |  email  |  victor@gmail       | False |
    |  email  |  victor@gmail.      | False |
    |  email  | victorius@gmail.com | True  |
    | phone   |  victor             | False |
    |    phone|  1234               | False |
    |    phone|  vic126             | False |
    |    phone|  0505820546         | True  |
    |    phone|  0642222224         | False |
    |    phone|  1234567890         | False |
    |    phone|052466546646652456882| False |
    |    phone|  050582054          | False |
    |    phone|  039179222          | True  |
    |    phone|  03-9179222         | True  |
    |    phone|  050-5820546        | True  |