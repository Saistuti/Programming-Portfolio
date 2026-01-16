import random

# Ask the user to enter their password
password = input("Enter your password: ")

# Check minimum length requirement
if len(password) < 9:
    print("Password too short.")
    exit()

# Perform three random character checks
for _ in range(3):
    # Choose a random position (1-based index)
    position = random.randint(1, len(password))

    # Ask the user for the character at that position
    guess = input(f"Enter letter at position {position}: ")

    # Check if the entered character matches the password
    if guess == password[position - 1]:
        print("Correct")
    else:
        print("\nSecurity check failed.")
        exit()

# If all checks pass
print("Security check passed.")
