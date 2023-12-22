@login
Feature: Login Feature

    @regression @positive
    Scenario: Success Login with correct credential

        Given I am on the homepage
        When I click Sign In
        Then Sign In page opens
        When I enter "dono@gmail.com" Email
        And  I enter "donodono12!" Password and Click Sign In
        Then I should be logged in


#    @negative
#    Scenario: Failed Login with [Blank Email] and [Random Password]
#
#        Given I am on the homepage
#        When I click Sign In
#        Then Sign In page opens
#        When I enter "" Email
#        And  I enter "yoyoko" Password and Click Sign In
#        Then I still in Customer Login Page
#        And Required Field Email message show up
#
#
#    @negative
#    Scenario: Failed Login with [Valid Email] and [Blank Password]
#
#        Given I am on the homepage
#        When I click Sign In
#        Then Sign In page opens
#        When I enter "dono@gmail.com" Email
#        And  I enter "" Password and Click Sign In
#        Then I still in Customer Login Page
#        And Required Field Password message show up
#
#
#    @negative
#    Scenario: Failed Login with [Valid Email] and [Invalid Password]
#
#        Given I am on the homepage
#        When I click Sign In
#        Then Sign In page opens
#        When I enter "dono@gmail.com" Email
#        And  I enter "123456" Password and Click Sign In
#        Then I still in Customer Login Page
#        And Error message show up
#
#
#    @negative
#    Scenario: Failed Login with [Invalid Email] and [Valid Password]
#
#        Given I am on the homepage
#        When I click Sign In
#        Then Sign In page opens
#        When I enter "blablablu@gmail.com" Email
#        And  I enter "donodono12!" Password and Click Sign In
#        Then I still in Customer Login Page
#        And Error message show up
#
#
#    @negative
#    Scenario: Failed Login with [Blank Email] and [Blank Password]
#
#        Given I am on the homepage
#        When I click Sign In
#        Then Sign In page opens
#        When I enter "" Email
#        And  I enter "" Password and Click Sign In
#        Then I still in Customer Login Page
#        And Required Field Email message show up
#        And Required Field Password message show up
#
#
#    @negative
#    Scenario: Failed Login with non-Existent credential
#
#        Given I am on the homepage
#        When I click Sign In
#        Then Sign In page opens
#        When I enter "blablablu@gmail.com" Email
#        And  I enter "blablablupassword" Password and Click Sign In
#        Then I still in Customer Login Page
#        And Error message show up
#
#
#    @negative
#    Scenario: Failed Login with [Invalid Email Format]
#
#        Given I am on the homepage
#        When I click Sign In
#        Then Sign In page opens
#        When I enter "blablablu" Email
#        And I enter "" Password and Click Sign In
#        Then I still in Customer Login Page
#        And Please enter a valid email address Error show up
