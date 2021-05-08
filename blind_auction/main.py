import os
import time
import sys
from art import logo

bidders_dict = {}
more_bidders = 'yes'
i = 0

def screen_clear():
    os.system('cls')

def blind_auction_game():
    print(f"{logo}\nHello... welcome to the secret bidding game.")

    bidders_dict = {
    "bidder_name": [],
    "bid_amount" : [],
    }
    more_bidders = 'yes'
    
    i = 0
    while more_bidders == 'yes':
        screen_clear()
        # asks for inputs until there is no more bidders
        name = input("What is your name?\n")
        bidders_dict["bidder_name"].append(name)
        bid = int(input("What is your bid?\n$"))
        bidders_dict["bid_amount"].append(bid)
        more_bidders = input("Are there any other bidders? 'yes' or 'no'\n").lower()
    
    if more_bidders == 'no':
        # finds the biggest number in bid_amount
        largest_num = 0
        for i in range(0, len(bidders_dict["bidder_name"])):
            if bidders_dict["bid_amount"][i] > largest_num:
                largest_num = bidders_dict["bid_amount"][i]
                incr_bidder = bidders_dict["bidder_name"][i]
                #incr_bid: gets the index of the largest num
                incr_bid = bidders_dict["bid_amount"].index(bidders_dict["bid_amount"][i])
                incr_bidder = incr_bidder.capitalize()
        # store the largest_num inside a temporary one because we will delete it (check next comment)
        temp_largest_num = largest_num
        # finds if there is a same bid amount as others
        # deletes the largest_num so that it can check if there is a similar one in
        # the dictionary ["bid_amount"].
        del bidders_dict["bid_amount"][incr_bid]

        #BUG: if there is a number bigger than the latest number it bugs out 
        if temp_largest_num in bidders_dict["bid_amount"]:
            screen_clear()
            retry_game = input(f"There is someone with the same bid as others, would you like to retry?\n 'yes' or 'no': ").lower()
            # Restart game or no?
            if retry_game == 'yes':
                print("Restarting...")
                blind_auction_game()
            elif retry_game == 'no':
                print("Terminating...")
                sys.exit()
        #If there isn't a similar one then
        else:
            print(f"{incr_bidder} won with the bid of ${temp_largest_num}!")


blind_auction_game()