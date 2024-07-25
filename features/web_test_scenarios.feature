@UI
Feature: Checkout functionality

  Scenario: Authorised user can Checkout with multiple items in the basket
    Given I am logged into the website
    When I add the following items to the basket
      | Product_title      | Size | Color |
      | Radiant Tee        | M    | Blue  |
      | Cronus Yoga Pant   | 32   | Blue  |
      | Compete Track Tote |      |       |
    And I proceed to checkout
    And I fill in the checkout details as follows
      | Field | First_name | Last_name | Email                | Street      | City    | State      | Zip_code | Country       | Phone      |
      | Value | John       | Doe       | john.doe@example.com | 123 Main St | Anytown | California | 90210    | United States | 1234567890 |
    And I select "free" delivery
    Then I confirm my order
    And I see correct order price