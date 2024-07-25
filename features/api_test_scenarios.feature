@API
Feature: API Interface Testing
  Background:
    Given I have a valid API token

Scenario: Create a booking and validate it
  Given I have the following booking details
    | field          | value         |
    | firstname      | Jane          |
    | lastname       | Doe           |
    | totalprice     | 150           |
    | depositpaid    | true          |
    | checkin        | 2022-02-01    |
    | checkout       | 2022-02-05    |
    | additionalneeds | Breakfast    |
  When I create a new booking
  Then I should be able to retrieve the booking and validate its content


  Scenario: Delete created booking
  Given I have the following booking details
    | field          | value         |
    | firstname      | Jane          |
    | lastname       | Doe           |
    | totalprice     | 150           |
    | depositpaid    | true          |
    | checkin        | 2022-02-01    |
    | checkout       | 2022-02-05    |
    | additionalneeds | Breakfast    |
  When I create a new booking
  Then I should be able to retrieve the booking and validate its content
  And I delete the booking
  And the booking should be deleted