import random
from os import system, name


def game():
    # Header, This is will show in start of program.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # guess_num function for guessing correct number.
    def guess_num(attempts):

        answer = random.randint(0, 100)
        # attempts = attempts
        while not attempts ==    -1:
            guess = int(input("Make a guess: "))
            if guess > answer and attempts != 0:
                print("Too high.")
                print("Guess again")
                print(f"You have {attempts} attempts remaining to guess the number.\n")

            elif guess < answer and attempts != 0:
                print("Too Low.")
                print("Guess again")
                print(f"You have {attempts} attempts remaining to guess the number.\n")

            elif guess == answer:
                print("You Win.\n")
                attempts = 0
                break
            else:
                print("You Loss.\n")
                attempts = 0
                break

            attempts -= 1

        # Difficulty level
        if difficulty_level == 'easy':
            # why i not take 10, beacause it print below line two time in program.
            attempts = 9
            print("You have 10 attempts remaining to guess the number.")
            guess_num(attempts)

        else:
            # why i not take 4, beacause it print below line two time in program.
            attempts = 4
            print("You have 5 attempts remaining to guess the number.")
            guess_num(attempts)


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


game()
# For restart the game.
run_again = input("Do you want to play again? 'y' or 'n': ")

if run_again == 'y':
    clear()
    game()
else:
    pass
