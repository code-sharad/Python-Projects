
# student_height = [156, 175, 165, 171, 187   ]

# total_height = 0
# for height in student_height:
#     total_height += height 
    

# number_of_students = 0
# for height in student_height:
#     number_of_students += 1

# print(total_height)
# # print(total_height / len(student_height))
# # print(round(total_height / len(student_height)))
# print(total_height / number_of_students)
# print(round(total_height / number_of_students))



# student_scores = [78, 65, 89, 55, 91, 64, 89]
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if highest_score < score:
#         highest_score = score
#     else:
#         pass

# print(f"The highest score in class is: {highest_score}.")
    

# total = []
# for number in range(1, 101):
#     if number % 2 == 0:
#         total.append(number)
# total.insert(0, 1)


# print(total)



# for number in range(1, 21):
#     if number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(number)


#Password Generator Project
import random
from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []
password = ' '

for i in range(nr_letters ):
    password_list.append(random.choice(letters))

for i in range(nr_symbols ):
    password_list.append(random.choice(symbols))

for i in range(nr_numbers ):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
for char in password_list:
    password += char
print(f"Here is you Password: {password}")
