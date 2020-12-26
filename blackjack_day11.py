############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Return random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.


def calculate_score(cards):
    """ Take a list of cards and returen score calculated from the cards."""
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game. 
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.   You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(21)
        cards.append(1)
    return sum(cards)

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if computer_score == user_score:
        return("Draw")
    elif computer_score == 0:
        return("Lose, opponent as Blackjack.")
    elif user_score == 0:
        return("Win with a Blackjack.")
    elif user_score > 21:
        return("You went over. You Lose.")
    elif computer_score > 21:
        return("Oppenent went over. You Win.")
    elif user_score > computer_score:
        return("You Win.")
    else:
        return("You Lose.")

def play_game():
    print(logo)
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, user score: {user_score}")
        print(f"    Computer First card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
        else:
        # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another cart, type 'n' to pass.")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

        # if is_game_over == False:
        #     draw_another_card = (input("You want to draw another card (y) yes and (n) no: "))

        #     if draw_another_card == 'y':
        #         user_cards.append(deal_card())
        #     else:
        #         is_game_over = True


    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.



    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card)
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}.")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}. ")
    print(compare(user_score, computer_score))

    

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
# of blackjack and show the logo from art.py.

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()

# logo = """
# .------.            _     _            _    _            _    
# |A_  _ |.          | |   | |          | |  (_)          | |   
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |                
#       `------'                           |__/           
# """

# want_to_play = input(
#     "Do you want to play a game of Blackjack? Type 'y' or 'n': ")


# def blackjack():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     user_player = [random.choice(cards), random.choice(cards)]
#     computer_card = [random.choice(cards), random.choice(cards)]

#     if want_to_play == 'y':
#         print(logo)
#         print(f"You're cards: {user_player}")
#         print(f"Computer first card: {computer_card[0]}")
#         another_card = input(
#             "Type 'y' to get  another card, type 'n' to pass: ")

#         while another_card == 'y' or sum(user_player) > 21:

#             if sum(user_player) > 21 or sum(computer_card) > 21:
#                 break
#             else:
#                 if another_card == 'y':
#                     # Adding random element from cards var to user and player var
#                     user_player += [random.choice(cards)]
#                     computer_card += [random.choice(cards)]

#                     if sum(user_player) > 21:
#                         print(
#                             f"Your final hand: {user_player} final score: {sum(user_player)} ")
#                         print(
#                             f"Computer final hand: {computer_card} final score: {sum(computer_card)} ")

#                         # another_card = 'n'

#                     elif sum(user_player) <= 21:
#                         # another_card = 'y'
#                         print(
#                             f"Your final hand: {user_player} final score: {sum(user_player)} ")
#                         print(
#                             f"Computer final hand: {computer_card} final score: {sum(computer_card)} ")

#                     elif sum(user_player) < 21:
#                         another_card = input(
#                             "Type 'y' to get  another card, type 'n' to pass: ")
#                 another_card = 'n'

#         # if another_card == 'n':
#         #     print(f"You're cards: {user_player}, current score: {total_computer_score}")
#         #     print(f"Computer first card: {computer_card[0]}")
#         #     print(f"Your final hand: {user_player} final score: {sum(user_player)} ")
#         #     print(f"Computer final hand: {computer_card} final score: {total_computer_score} ")

#         # total_computer_score = sum(computer_card)
#         # total_user_score = sum(user_player)

#         print(f"You're cards: {user_player}, score: {sum(user_player)}")
#         print(f"Computer cards: {computer_card}, score: {sum(computer_card)}")

#         if sum(computer_card) < 21 and sum(user_player) < 21:
#             if computer_card > user_player:
#                 print("You Lose")
#             elif sum(computer_card) == sum(user_player):
#                 print("Draw")
#             else:
#                 print("You Win")

#         elif sum(computer_card) > 21 and sum(user_player) > 21:
#             if sum(computer_card) == sum(user_player):
#                 print("Draw")
#             else:
#                 print("You Lose!")
#         elif sum(user_player) <= 21:
#             if sum(user_player) < 21 and sum(computer_card) < 21:

#         elif sum(computer_card) == sum(user_player):
#             print("Draw")


# blackjack()
