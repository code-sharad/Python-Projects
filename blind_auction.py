# import os

# clear = lambda: os.system('clear')


class Wipe(object):
    def __repr__(self):
        return '\n' * 1000


wipe = Wipe()

bidding_finished = False
highest_bid = 0
winner = ""
bids = {}


def find_highest_bidder(bidding_record):
    global highest_bid
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f" The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("Enter your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print(wipe)
        # bidding_finished = True
