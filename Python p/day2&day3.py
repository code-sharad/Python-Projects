# user_num = input("Enter two digit number: ")
# num1 = user_num[0]
# num2 = user_num[1]

# result = int(num2) + int(num1)
# print(result)


# weight = int(input("enter your weight in kg: "))
# height = float(input("enter your height in m:" ))

# bmi = round(weight / height ** 2)
# print(round(bmi))
# if bmi < 18.5:
#     print(f"You BMI is {bmi}, you are slightly underweight.")
# elif 18.5 < bmi > 25:
#     print(f"You BMI is {bmi}, you are slightly normal weight.")
# elif 25 < bmi > 30:
#     print(f"You BMI is {bmi}, you are slightly overweight.")
# else:
#     print(f"You BMI is {bmi}, you are clinically obese.")

# year = 1
# month = 12
# days = 365
# weeks = 52

# age = int(input("What is your current age? "))
# cal = 90 - age
# remaining_year_to_live = cal * year
# remaining_months_to_live = cal * month
# remaining_weeks_to_live = cal * weeks
# remaining_days_to_live = cal *days

# print(f"You have {remaining_days_to_live} days, {remaining_weeks_to_live} weeks, {remaining_months_to_live} months left.")



# year = int(input("enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print("This is not leap year.")
#     else:
#         print(f"{year} is leap year.")
# else:
#     print("This is not leap year.")



# Love Score

# name1 = input("Enter your name: ").lower()
# name2 = input("Enter your name: ").lower()



# combined_string = name1 + name2

# t = combined_string.count('t')
# r = combined_string.count('r')
# u = combined_string.count('u')
# e = combined_string.count('e')

# true = t + r + u + e 

# l = combined_string.count('l')
# o = combined_string.count('o')
# v = combined_string.count('v')
# e = combined_string.count('e')

# love = l + o + v + e 
# love_score = int(str(true)+str(love))
# print(love_score)


# if (love_score < 10) or (love_score > 90):
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <= 50):
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Nikhil]
*******************************************************************************
''')

print("Welcome to treasure Island")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if choice1 == 'right':
    print("You fell into a hole. Game over.")

elif choice1 == 'left':
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 == 'swim':
        print("Game Over.")
    elif choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == 'blue':
            print("Game Over.")
        elif choice3 == 'red':
            print("Game Over.")
        elif choice3 == 'yellow':
            print("You Win!")

