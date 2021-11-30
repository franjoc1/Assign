Feature: Python test to send GET request and validate response using BDD

Scenario: GET request example 1
    Given Set GET API endpoint
    When GET request is sent to API
    Then Valid HTTP response should be received
    And Response http code should be 200

@tag2
Scenario: Change Currency Param
    Given Set GET API endpoint with changed EUR Param
    When GET request is sent to API
    Then Valid HTTP response should be received
    And Response http code should be 200
    And Param should be changed to EUR