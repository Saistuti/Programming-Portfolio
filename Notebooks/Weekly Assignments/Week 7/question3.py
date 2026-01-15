'''
This program stores countries and their capital cities.
It asks the user to enter a country name.
If the capital is known, it displays it.
Otherwise, it asks the user to enter the capital.
The program continues until the user chooses to quit.
Country names are handled case-insensitively.
'''

capitals = {}

while True:
    country = input("Enter a country: ").strip()

    if country == "":
        break

    key = country.lower()

    if key in capitals:
        print(f"The capital of {country.title()} is {capitals[key]}.")
    else:
        capital = input(f"I don't know the capital of {country.title()}. Please enter it: ")
        capitals[key] = capital
        print("Thank you. Capital stored.")