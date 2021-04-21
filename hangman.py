#ssStep 1 

word_list = ["aardvark", "baboon", "camel"]

#DONE-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

random_word = random.choice(word_list)
chosen_word = random_word

#DONE-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#guess = input("Guess a letter")
#guess.lower()

#DONE-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
def split(random_word):
    return list(random_word)

split_random_word = split(random_word)

life = 5

final_guess_word = ""

while life > 0 :
    guess = input("Guess a letter: ")
    guess.lower()
    
    guessed_a_letter = None
    
    for i in range(0, len(split_random_word)):
        if guess == split_random_word[i]:
            guessed_a_letter = True
            print("You guessed a letter!")
            
    if not guessed_a_letter:
        for i in range(0, len(split_random_word)):
            if guess != split_random_word[i]:
                life -= 1
                print("You lost a life")
                break

    
    if final_guess_word == random_word:
        print("Congrats! you guessed the word")

