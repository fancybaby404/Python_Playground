import random
from hangman_words import word_list
from hangman_art import stages, logo, bruh_logo, ok_sign_logo
import os

def screen_clear():
    os.system('cls')

def split(random_word):
    return list(random_word)

random_word = random.choice(word_list).lower()
chosen_word = random_word
split_random_word = split(random_word)
lives = 6
test_guess_word = ""
final_guess_word = ""
display = []
every_guessed_word = []


print(logo)                                        


for i in split_random_word:
    display += "_"

while lives > 0 :
    
    print(stages[lives])
    print("\n")
    print(f"pssssssst.. the word is : {random_word}")
    guess = input("Guess a letter: ").lower()
    every_guessed_word.append(guess)
    guessed_a_letter = False
    already_guessed = False
    
    if guess in display:
        already_guessed = True
        screen_clear()
        print(f"You've already guessed the letter '{guess}' try a different one.")
    
    if not already_guessed:
        for i in range(0, len(split_random_word)):   
            if guess == split_random_word[i]:
                display[i] = guess
                guessed_a_letter = True
                screen_clear()
                print("You guessed a letter!\n")
                
        if not guessed_a_letter:    
            if not guess in split_random_word:
                screen_clear()
                print("You entered the wrong letter.\n")
                lives -= 1
    
        
    final_guess_word = "".join(display)
    
    print(f"What you have currently guessed : {final_guess_word}")
    print(f"You have {lives} lives left")

    if lives <= 0:
        screen_clear()
        print(f'''You lose.\nThe word was '{chosen_word}'\n{bruh_logo}''')
        break
        
    if final_guess_word == random_word:
        screen_clear()
        print(f'''You won!\nThe final word is '{chosen_word}'\n{ok_sign_logo}''')
        break