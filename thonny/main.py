




#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
import random
from hangman_words import word_list
from hangman_art import stages
import os

def screen_clear():
    os.system('cls')

def split(random_word):
    return list(random_word)

random_word = random.choice(word_list).lower()
chosen_word = random_word
split_random_word = split(random_word)
lives = 6
final_guess_word = ""
display = []

logo = ''' 
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/    '''
print(logo)                                        

#print(f"pssssssst.. the word is : {random_word}")
for i in split_random_word:
    display += "_"

while lives > 0 :
    
    print(stages[lives])
    print("\n")
    guess = input("Guess a letter: ")
    guess.lower()
    guessed_a_letter = False

    for i in range(0, len(split_random_word)):
        if guess == split_random_word[i]:
            display[i] = guess
            guessed_a_letter = True
            screen_clear()
            print("You guessed a letter!\n")

    if not guessed_a_letter:    
        if guess in split_random_word:
            screen_clear()
            print(f"You've already guessed {guess}\n")
        if not guess in split_random_word:
            screen_clear()
            print("You entered the wrong letter.\n")
            lives -= 1
    
           
    final_guess_word = " ".join(display)

    print(f"What you have currently guessed : {final_guess_word}")
    print(f"You have {lives} lives left")

    if lives <= 0:
        screen_clear()
        print('''You lose.\n
        
██████╗░██████╗░██╗░░░██╗██╗░░██╗
██╔══██╗██╔══██╗██║░░░██║██║░░██║
██████╦╝██████╔╝██║░░░██║███████║
██╔══██╗██╔══██╗██║░░░██║██╔══██║
██████╦╝██║░░██║╚██████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝
        
        ''')
        break
    if final_guess_word == random_word:
        screen_clear()
        print('''You won!\n
        
                   .__    _
           @ V; .Z~M
          || :|:@  d
          d' d\@  jf
   .*\   :P  #P  |P
   M `|  W  .@   Z
   | .b :!  d'  W'
   |  V W   #  .W**=m_
    |  !||   @  W'_   ~V;
    ||  M| _ Nm4| YmjL|PN_
     #   W#~    YN_W'YL#W#b
     |;  +       |f   `#'#8L
     W        ._#L_  .#,`'||
     |,     .WMP' ~Mm#`Nm;d|
     `|       W   Mmd#; .df
      |       M    `M#@-W'
      W       !b     WtZ'
      M        V;    |P
      ||        b   .@
       D        Y| .W'
      j|         'j@'
     jP'  L_mq=-_@'
   .Z!         jf
  mf         .W'
            .@'
           .@'
          .@
         :@
        
        
        '''
        )
        break