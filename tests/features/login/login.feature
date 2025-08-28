@e2e @login

Feature: Login Feature
            """
            As a user, I want to log in to the application so that I can access my dashboard.
            """

    Background: Background name
        Given the user is on the login page

    @positive_scenario @smoke
    Scenario: Successful Login
        When the user enters valid credentials
        Then the login is successful

    # @negative_scenario @smoke
    # Scenario: Unsuccessful Login with Invalid Credentials
    #     When the user enters invalid credentials
    #     Then an error message should be displayed