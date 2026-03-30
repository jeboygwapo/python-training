import os
def get_bid_info():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_db[name] = bid
    return bid_db

def get_winner():
    highest_bid = max(bid_db.values())
    for winner in bid_db:
        if highest_bid == bid_db[winner]:
            print(f"The winner is {winner} with a bid of ${highest_bid}")
            break

def other_bidders():
    ask_other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if ask_other_bidders == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    elif ask_other_bidders == 'no':
        get_winner()
        return False
    else:          
        print("Invalid input, please try again.\n")

print("Welcome to the secret auction program.")
session = True
bid_db = {}

while session:
    get_bid_info()
    session = other_bidders()

