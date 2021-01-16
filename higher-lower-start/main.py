from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Use if statement to check  if user is correct ana returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make repeatable
while game_should_continue:
    # Generate a random account from the game data.
    # Making account at position B become next account position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format.
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

    # Ask user for a guess.
    guess = (input("Who as you're follower, Type 'A' or 'B': ")).lower()
    # Check if user is correct
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print("You're right.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
