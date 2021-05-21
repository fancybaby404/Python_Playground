from guessthenumber_art import logo
from guessthenumber_art import among_us
from guessthenumber_art import istupid
import random
import os

def screen_clear():
    os.system('cls')

def play_again():
    play_again = input("Do you want to play another game? Type 'y' or 'n': ")
    if play_again == 'y':
        guessing_game()
    elif play_again == 'n':
        exit()

def guessing_game():
    # Initialization
    screen_clear()
    attempts = 0
    NUM_TO_GUESS = random.randint(0,100)

    print(logo)
    print(f"Welcome to the Number Guessing Game!\nIm thinking of a number between 1 and 100.")
    chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # Attempts 
    if chosen_difficulty == 'easy':
        attempts = EASY_ATTEMPTS
    elif chosen_difficulty == 'hard':
        attempts = HARD_ATTEMPTS
    else:
        print("You've entered an invalid input")
        return

    # Start of the game
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number")
        guess = input("Make a guess: ")

        # Checks if the guess input is not a number
        if not guess.isdigit():
            print(f"Please enter a number.\n")
            continue
        
        # Guess too low
        if int(guess) < int(NUM_TO_GUESS):
            print(f"Too low")
            attempts -= 1
        # Guess too high
        if int(guess) > int(NUM_TO_GUESS):
            print(f"Too high")
            attempts -= 1

        # Winning statement
        if int(guess) == NUM_TO_GUESS:
            print("Congratulation you guessed the number!")
            print(f"{among_us}\nWoah woah.. you kinda sus..")
            print(f"Number you guessed: {NUM_TO_GUESS}")
            play_again()
    # Losing statement
    print(f"You lost, the number to guess was {NUM_TO_GUESS}\n{istupid}")
    play_again()
# --------------------------------------------- END OF CODE ---------------------------------------------
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
guessing_game()

