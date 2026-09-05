Feature: Login
   Login functinality validation
@smoke,@regression
Scenario: Verify login with valid credentails
Given User opens the application
When User enters credentails
Then User should login successfully

Scenario: Unsuccessful login with invalid credentials
Given User opens the application
When User enters invalid  credentails
And clicks  the login button
Then the user should see an error message