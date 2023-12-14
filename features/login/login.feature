@login
Feature: Login Feature

    @regression @positive
    Scenario: Success Login with correct credential

        Given I am on the homepage
        When I click Sign In
        Then Sign In page opens
        When I enter dono@gmail.com Email
        And  I enter donodono12! Password and Click Sign In
        Then I should be logged in
