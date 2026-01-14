'''
This program calculates how many lab groups can be formed from a given
number of students and a required group size.
It uses integer division to find the number of full groups
and the modulus operator to find how many students are left over.
The program also fixes grammar for 'student' or 'students' in the output.
'''

students = int(input("How many students? "))
group_size = int(input("Required group size? "))

groups = students // group_size
leftover = students % group_size

student_word = "student" if leftover == 1 else "students"

print(f"There will be {groups} groups with {leftover} {student_word} left over.")