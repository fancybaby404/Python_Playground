############### Blackjack Project #####################

#😂Difficulty Normal 😎: Use all Hints below to complete the project.
#😂Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#😂Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#✅Difficulty Expert 🤯: Only use Hint 1 to complete the project.
# DID DIFFICULTY EXPERT MUHAHAHA 😂😂🤣🤣
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### START #####################
import random
import os
from blackJack_art import logo

def randomCards(cards, user_cards, computer_cards, total_user_cards, total_computer_cards):
    while len(user_cards) != 2 and len(computer_cards) != 2:
        randomInteger = random.randint(0, len(cards) -1)
        user_cards.append(cards[randomInteger])
        removeItem(cards, randomInteger)
        total_user_cards = sum(user_cards)
        #(USERCARDS)BLACK JACK: check if cards are 11 and 10, which makes the total amount card  to 0
        if sum(user_cards) == 21  and len(user_cards) == 2:
            total_user_cards == 0

        randomInteger = random.randint(0, len(cards) -1)
        computer_cards.append(cards[randomInteger])
        removeItem(cards, randomInteger)
        total_computer_cards = sum(computer_cards)

        #(COMPUTERCARDS)BLACK JACK: check if cards are 11 and 10, which makes the total amount card  to 0
        if sum(computer_cards) == 21  and len(computer_cards) == 2:
            total_computer_cards == 0
            
    return user_cards, computer_cards
    #        randomChoice = random.choice(cards)
    #        user_cards.append(randomChoice)
    #        computer_cards.append(randomChoice)

def removeItem(list, index):
    list.pop(index)
    return list

def getCard(cards, person): 
    """appends a random card to the second parameter(person)"""
    randomInteger = random.randint(0, len(cards) - 1)
    person.append(cards[randomInteger])
    removeItem(cards, randomInteger)
    #     randomChoice = random.choice(cards)
    #     return person.append(randomChoice)

def getTotal(user_cards, total_user_cards, computer_cards, total_computer_cards):
    print(f"\nGame has ended, final results:\n    Your final hand: {user_cards}, final score = {total_user_cards},\n    Computer's final hand: {computer_cards}, final score: {total_computer_cards}")

def play_again():
    
    play_blackjack = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if play_blackjack == 'y':
        screen_clear()
        blackjack()
    elif play_blackjack == 'n':
        exit()

def screen_clear():
    os.system('cls')

def compare_cards(user_cards, computer_cards, total_user_cards, total_computer_cards):    
    #tie   
    if total_computer_cards == total_user_cards or total_user_cards == total_computer_cards:
        getTotal(user_cards, total_user_cards, computer_cards, total_computer_cards)
        print("It's a draw! 😮")
        return play_again()
    #blackjack:
    elif total_user_cards == 0:
        getTotal(user_cards, total_user_cards, computer_cards, total_computer_cards)
        print(f"Won with a BlackJack! 😲 SHEESH")
        return play_again()
    elif total_computer_cards == 0:
        getTotal(user_cards, total_user_cards, computer_cards, total_computer_cards)
        print(f"Lost, opponent has Blackjack 😱")
        return play_again()

    #if user's cards are exactly 21
    elif total_user_cards == 21:
        getTotal(user_cards, total_user_cards, computer_cards,total_computer_cards)
        print(f"You Won! 🤯")
        return play_again()

    #computer over 21 (WIN)
    elif total_computer_cards > 21:
        getTotal(user_cards, total_user_cards, computer_cards, total_computer_cards)
        print("Computer went over! You won! 🤯")
        return play_again()

    #lose
    elif total_computer_cards > total_user_cards:
        getTotal(user_cards, total_user_cards, computer_cards, total_computer_cards)
        print("You lost 😤")
        return play_again()
    
    #win
    elif total_user_cards > total_computer_cards:
        getTotal(user_cards, total_user_cards, computer_cards, total_computer_cards)
        print("You won! 🤯")
        return play_again()

def ace_card(card, total_card):
    if 11 in card and total_card > 21:
        print("    Ace card found! Turning it's value to 1")
        card.remove(11)
        card.append(1)
        total_card = sum(card)

def blackjack():
    screen_clear()
    #defining of variables
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    total_computer_cards = 0
    total_user_cards = 0
    computer_black_jack = False

    #randomizing the content of cards
    randomCards(cards, user_cards,computer_cards, total_user_cards, total_computer_cards)
    total_user_cards = sum(user_cards)
    total_computer_cards = sum(computer_cards)

    #(USERCARDS)BLACK JACK: check if cards are 11 and 10, which makes the total amount card  to 0
    if sum(user_cards) == 21  and len(user_cards) == 2:
        total_user_cards = 0   
    #(COMPUTERCARDS)BLACK JACK: check if cards are 11 and 10, which makes the total amount card  to 0
    if sum(computer_cards) == 21  and len(computer_cards) == 2:
        total_computer_cards = 0
        computer_black_jack = True

    print(logo)
    print(f"    Your cards: {user_cards}, current score: {total_user_cards}\n    Computer's first card: {computer_cards[0]}")

    #hit or pass
    another_card = 'y'
    if another_card == 'y':
        while(another_card == 'y'):
            # user picks if they want to get another card
            another_card = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                #add card:
                getCard(cards, user_cards)
                total_user_cards = sum(user_cards)

                #ace card:
                ace_card(user_cards, total_user_cards)
                total_user_cards = sum(user_cards)
                print(f"    Your cards: {user_cards}, current score: {total_user_cards}\n    Computer's first card: {computer_cards[0]}")
            elif another_card == 'n':
                pass

            #get a new card if computer cards is less than 17
            if total_computer_cards < 17 and not computer_black_jack:
                #get card:
                getCard(cards, computer_cards)
                total_computer_cards = sum(computer_cards)

                # ace card:
                ace_card(computer_cards, total_computer_cards)
                total_computer_cards = sum(computer_cards)

            #if user cards above 21
            if total_user_cards > 21:
                getTotal(user_cards, total_user_cards, computer_cards, total_computer_cards)
                print(f"You went over. You lost 😭")
                return play_again()


    compare_cards(user_cards, computer_cards, total_user_cards, total_computer_cards)

blackjack()

##################### END #####################

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

