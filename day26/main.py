# For Loop
number = [1, 2, 3]
new_list = []
for n in number:
    add_1 = n + 1
    new_list.append(add_1)

# List Compression
new_list = [n + 1 for n in number]

# String as List
name = "Nikhil"
letter_list = [letter for letter in name]

# Range as List
range_list = [n * 2 for n in range(1, 5)]

# Condition List Comprehension
names = ["Alex", "Both", "Caroline", "Dave", "Elnar", "Freddie"]
long_list = [name.upper() for item in name if len(name) < 5]

upper_case_names = [name.upper() for name in name if len(name) > 4]

# Dictionary Comprehension

import random

student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_student = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_student)
