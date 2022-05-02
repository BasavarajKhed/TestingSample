Feature: validate login

  Scenario Outline: verify with dynamic data
    Given i am in login page with username & password
    When i enter "<user>" and "<pwd>"
    And  click on submit
    Then verify the title of the page


    Examples:
      | user   |  | pwd    |
      | robert |  | robert |
      | john   |  | john   |
      | joel   |  | joel   |