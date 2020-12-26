# import random
# from random import randint

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = random.random()
# random_float = random_float * 5
# print(random_float)

# test_seed = int(input('Create a seed number: '))
# random.seed(test_seed)
# random_num = random.randint(0,1)
# if random_num == 1:
#     print("Head")
# else:
#     print("Tail")


# from os import name
# import random
# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
# names = namesAsCSV.split(", ")
# # print(names)
# # names_items = len(names)
# # random_choice = random.randint(0, names_items - 1)
# # person_who_will_pay = names[random_choice]
# person_who_will_pay = random.choice(names)
# print(f"{person_who_will_pay} is going to buy meal today!")



# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# mylist =[
#  [" "," "," "],
#  [" "," "," "],
#  [" "," "," "]
# ]

# position =input("Where do you want to put tresure? ").split()

# column = int(position[0][0]) -1
# row = int(position[0][1]) -1

# mylist[row][column] = 'X'


# print(f"{mylist[0]}\n{mylist[1]}\n{mylist[2]} ")

import random

user = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors."))
computer = random.randint(0,2)

if user == 0:

    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
    print(rock)
    if computer == 0:
        print("Tie")
    elif computer == 1:
        print("You Lose!")
    elif computer == 2:
        print("You Win!")
    



elif user == 1:
    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''
    print(paper)
    if computer == 0:
        print("You Win!")
    elif computer == 1:
        print("Tie")
    elif computer == 2:
        print("You Lose!")
elif user == 2:
    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
    print(scissors)
    if computer == 0:
        print("You Lose!")
    elif computer == 1:
        print("You Win!")
    elif computer == 2:
        print("Tie")
    

else:
    print("Run again!")