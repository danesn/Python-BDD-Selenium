@endtoend
Feature: EndToEnd Buy Product

  Scenario: Buy a Product from Collection Shop

    Given I have Logged In and I am on the Home Page
    When I Click Shop New Yoga button
    Then Page Title Heading the collection appears
    And There are items on the page have at least 1 item or more
    When I Click an Item on Product List
    Then Detail Page about the Product appears
    And I Makesure the Product In Stock
    When I Choose Size, Color, and Quantity the Product
    And I Click Add to Cart button
    Then The Product Success Added to Shopping Cart
    When I Go to the Shopping Cart
    Then Shopping Cart Page appears
    And I Verify the Product data is Valid
    When I Click Proceed to Checkout button
    Then Shipping Address appears
    And I Verify the Product from Order Summary is Valid
    When I Click + New Address button
    Then Shipping Address Modal appears
    When I Filled Shipping Address correctly
    And I Click Ship here button
    Then The New Added Address show up
    When I Choose Shipping Methods
    And I Click Next button
    Then Payment Method appears
    And I Verify the Order Summary and the Address
    When I Check my billing and shipping address are the same
    And I Click Place Order button
    Then The Order should be successful