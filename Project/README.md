# Project
## Task 1: Beckett Pizza Plaza – 4-for-3 Offer Calculator
This task focuses on using a computer program to automate such a calculation. By applying basic programming concepts such as user input, validation, calculations, and output formatting, the program ensures that the final order price is calculated accurately and consistently. Pizza takeaway pricing can be complicated due to discounts and special offers.
Beckett Pizza Plaza (BPP) offers a 4-for-3 deal, where customers must order exactly four pizzas, and the cheapest pizza is free.
The purpose of this program is to calculate the total price of an order under this offer and display the discount achieved.

### Program Description:
This Python program:
1. Prompts the user to enter the prices of four pizzas
2. Validates each input to ensure it is a positive numeric value
3. Applies the 4-for-3 discount by removing the cheapest pizza price
4. Calculates:
    - The final order total
    - The percentage discount achieved (maximum 25%)
    - Displays the result clearly to the user
    - The program also handles incorrect input gracefully by displaying an error message and requesting valid input.

### How The Program Works:
1. The program displays a heading for Beckett Pizza Plaza.
2. The user is prompted to enter the price of each pizza.
3. If an invalid price is entered (non-numeric, zero, or negative), the user is asked to re-enter the price.
4. Once four valid prices are entered:
    - The cheapest pizza is excluded
    - The remaining three prices are summed
    - The discount percentage is calculated
- The final total and discount are displayed.

## Task 2: Password Verification Program
This program simulates a simple password security check. It first verifies that a password meets a minimum length requirement, and then performs additional verification by asking the user to confirm specific characters from the password.

### Program Description:
The program works in two stages:

1. Password Length Check
- The user is prompted to enter a password.
- If the password is less than 9 characters long, the program informs the user that the password is too short and exits.

2. Security Verification Check
- If the password length is valid, the program randomly selects three positions within the password.
- The user is asked to enter the character at each specified position.
- If any character is entered incorrectly, the program immediately exits and reports a failure.
- If all three checks are correct, the program reports that the security check has passed.

The same position may be requested more than once, as allowed by the task specification.

### How The Program Works:
- The user enters a password.
- If the password is shorter than 9 characters, the program exits.
- The program then asks for three random characters from the password.
- If any answer is incorrect, the program stops.
- If all answers are correct, the security check passes.
