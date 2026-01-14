'''
This program helps a teacher distribute sweets among pupils.
It asks for the total number of sweets and the number of pupils present.
Using integer division, it calculates how many sweets each pupil receives.
Using the modulus operator, it calculates how many sweets are left over.
The results are then displayed to the user.
'''

sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are present? "))

each = sweets // pupils
leftover = sweets % pupils

print(f"Each pupil gets {each} sweets.")
print(f"There will be {leftover} sweets left over.")



