import random

def split(random_word):
    return list(random_word)
word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list).lower()
chosen_word = random_word
split_random_word = split(random_word)
life = 5
final_guess_word = ""
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
display = []

for i in split_random_word:
    display += "_"

print(display)

while life > 0 :
    guess = input("Guess a letter: ")
    guess.lower()
    
    guessed_a_letter = None
    
    num_repeat = 0

    #BUG:
    for i in range(0, len(split_random_word)):
        #if display[num_repeat] in display:
        #    display[num_repeat] == guess
        if guess == split_random_word[i]:
            guessed_a_letter = True
            print(display)
            print("You guessed a letter!")
        num_repeat += 1
                
    if not guessed_a_letter:
        for i in range(0, len(split_random_word)):
            if guess != split_random_word[i]:
                life -= 1
                print("You lost a life")
                break

#TODO's:
#DONE-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be 
# ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.



#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.