"""
Beckett Pizza Plaza - 4-for-3 Offer Calculator

This program calculates the total cost of a pizza order
using Beckett Pizza Plaza's four-for-three discount offer.
"""

# Display Program Header

def display_header():
    """
    Prints the program title and separator.
    """
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================")


# Input Validation Helpers

def is_valid_price(value):
    """
    Checks whether the given value is a valid pizza price.
    A valid price must be a positive number.
    """
    try:
        price = float(value)
        return price > 0
    except ValueError:
        return False


def get_price(pizza_number):
    """
    Prompts the user to enter the price of a pizza.
    Repeats until the user enters a valid price.
    """
    while True:
        user_input = input(f"Enter Price of Pizza #{pizza_number}: ")

        # Validate the user input before converting
        if not is_valid_price(user_input):
            print("Please enter a valid price!")
            continue

        return float(user_input)


# Collect Pizza Prices

def collect_prices():
    """
    Collects prices for exactly four pizzas.
    """
    prices = []

    # Loop exactly four times
    for i in range(1, 5):
        price = get_price(i)
        prices.append(price)

    return prices


# Calculation Functions

def calculate_total(prices):
    """
    Calculates the total payable amount.
    The cheapest pizza is free under the 4-for-3 offer.
    """
    cheapest_pizza = min(prices)
    total = sum(prices) - cheapest_pizza
    return total


def calculate_discount_percentage(prices):
    """
    Calculates the percentage discount achieved.
    """
    cheapest_pizza = min(prices)
    original_total = sum(prices)

    discount_percentage = (cheapest_pizza / original_total) * 100
    return discount_percentage



# Output Display

def display_result(total, discount):
    """
    Displays the final total and discount.
    """
    print()
    print(f"Order Total is £{total:.2f}, a fabulous discount of {discount:.0f}%!")



# Main Program Logic

def main():
    """
    Main entry point of the program.
    """
    display_header()

    # Get pizza prices from the user
    prices = collect_prices()

    # Perform calculations
    total_price = calculate_total(prices)
    discount = calculate_discount_percentage(prices)

    # Show the result
    display_result(total_price, discount)


# Program Execution

if __name__ == "__main__":
    main()
