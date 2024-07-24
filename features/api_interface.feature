@API
Feature: API Interface Testing

  Scenario: Verify API character details
    Given I make a GET request to "/people/1"
    Then the response status code should be 200
    And the response should include "name": "Luke Skywalker"
    And the response should match the character model

  Scenario: Verify API planet details
    Given I make a GET request to "/planets/1"
    Then the response status code should be 200
    And the response should include "name": "Tatooine"
    And the response should match the planet model

  Scenario: Verify API film details
    Given I make a GET request to "/films/1"
    Then the response status code should be 200
    And the response should include "title": "A New Hope"
    And the response should match the film model

  Scenario: Verify API species details
    Given I make a GET request to "/species/1"
    Then the response status code should be 200
    And the response should include "name": "Human"
    And the response should match the species model