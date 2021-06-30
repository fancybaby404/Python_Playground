from tkinter import *
import pandas as pd
from random import choice, randint
import json

# GLOBALS
BACKGROUND_COLOR = "#B1DDC6"
index = {}
wrong_button_pressed = True
right_button_pressed = True

reading_japanese_file = True
reading_learn_file = True

# ------------------- ...READ JSON FILE... -------------------- #
# You have to change the indices | Japanese -> 1 | English -> 2 |
jp_words_DATA = pd.read_json('data/japanese_words.json').to_dict(orient='records')

# ------------------- Words To Learn -------------------------- #
column_names = ['Japanese', 'English']

learn_index = 0
try:
    learn_file = pd.read_csv('./words_to_learn.csv', encoding='utf-8', names=column_names)
except FileNotFoundError:
    with open(file='words_to_learn.csv', mode='w', encoding='utf-8') as data_file:
        data_file.write('')
    learn_file = pd.read_csv('./words_to_learn.csv', encoding='utf-8', names=column_names)
# Wrong button
def wrong_button():
    global index
    global learn_index
    global learn_file
    
    global reading_japanese_file
    global reading_learn_file   
    
    # Check if file exists
    file_found = False
    try:
        with open(file='words_to_learn.csv', mode='r', encoding='utf-8') as data_file:
            data_file.read()
    except FileNotFoundError:
        file_found = False
    
    # Put the current cards into words_to_learn.csv
    with open(file='words_to_learn.csv', mode='a', encoding='utf-8') as data_file:        
        learn_file = pd.read_csv('./words_to_learn.csv', encoding='utf-8', names=column_names)
        # if the file is found use the index of the words_to_learn 
        # to append the current card:
        
        # Append from japanese_words.json
        if reading_japanese_file and not file_found and len(learn_file.index) <= 5:
            japanese = index['Japanese']
            english = index['English']
            data_file.write(f'{japanese},{english}\n')
        # Append from words_to_learn.csv
        elif reading_learn_file and file_found and len(learn_file.index) >= 5:
            try:
                row = learn_file.loc[learn_index]
            except KeyError:
                return
            japanese = row['Japanese']
            english = row['English']
            data_file.write(f'{japanese},{english}\n')
    
    global wrong_button_pressed
    wrong_button_pressed = True
    random_card()

def right_button():
    global learn_file
    global learn_index
    global reading_japanese_file
    global reading_learn_file
    
    # Check if file exists
    file_found = False
    try:
        with open(file='words_to_learn.csv', mode='r', encoding='utf-8') as data_file:
            data_file.read()
        file_found = True
    except FileNotFoundError:
        file_found = False 
    
    # If the file is found and the amount of lines is greater than or equal to 5:
    learn_file = pd.read_csv('./words_to_learn.csv', encoding='utf-8', names=column_names)
    if reading_learn_file and file_found and len(learn_file.index) >= 5:
        # update words_to_learn:
        learn_file = pd.read_csv('./words_to_learn.csv', encoding='utf-8', names=column_names)
        
        # Removes from words_to_learn
        with open("words_to_learn.csv", "r", encoding='utf-8') as f:
            lines = f.readlines()
        try:
            with open("words_to_learn.csv", "w", encoding='utf-8') as f:
                row = learn_file.loc[learn_index]
                japanese = row["Japanese"]
                english = row["English"]
                for line in lines:
                    if line.strip('\n') != f'{japanese},{english}':
                        f.write(line)
        except KeyError:
            print('already removed')
    else:
        print('reading japanese file, canceling...')

    global right_button_pressed
    right_button_pressed = True
    random_card()
    
# -------------------- READING DATA -------------------- #
def random_card():
    global learn_file
    global learn_index
    
    global wrong_button_pressed
    global right_button_pressed
    
    global reading_japanese_file
    global reading_learn_file
    
    if not wrong_button_pressed or not right_button_pressed:
        pass
    else:
        # --- Check if file exists --- #
        file_found = False
        try:
            with open(file='words_to_learn.csv', mode='r', encoding='utf-8') as data_file:
                data_file.read()
                file_found = True
        except FileNotFoundError:
            file_found = False
        # ---------------------------- #
        
        if not file_found or len(learn_file.index) <= 5:
            # Read japanese_words.json
            reading_japanese_file = True
            print('reading from japanese_words')
            global index
            index = choice(jp_words_DATA)
            
            japanese = index['Japanese']
            
            card_canvas.itemconfig(language_label, text="Japanese", fill='black')
            card_canvas.itemconfig(word_label, text=f'{japanese}', fill='black')
            card_canvas.itemconfig(card_image, image=card_front_image)
        else:
            # Read words_to_learn.csv
            reading_learn_file = True
            print('reading from words_to_learn')
            learn_index = randint(0, len(learn_file.index) - 1)
            print(f'\n{learn_index=}')
            row = learn_file.loc[learn_index]
            print(f'\n{row=}')
            japanese = row['Japanese']
            
            # Change Labels
            card_canvas.itemconfig(language_label, text="Japanese", fill='black')
            card_canvas.itemconfig(word_label, text=f'{japanese}', fill='black')
            card_canvas.itemconfig(card_image, image=card_front_image)

        window.after(3000, flip_card)

# -------------------- FLIP CARD -------------------- #
def flip_card():
    global learn_file
    global learn_index
    
    # --- Check if file exists --- #
    file_found = False
    try:
        with open(file='words_to_learn.csv', mode='r', encoding='utf-8') as data_file:
            data_file.read()
            file_found = True
    except FileNotFoundError:
        file_found = False
    # ---------------------------- #

    if not file_found or len(learn_file.index) <= 5:
        global index
        global jp_words_DATA
        english = index['English']
        
        # Change labels
        card_canvas.itemconfig(card_image, image=card_back_image)
        card_canvas.itemconfig(language_label, text="English", fill='white')
        card_canvas.itemconfig(word_label, text=f'{english}', fill='white')
    else:
        row = learn_file.loc[learn_index]
        english = row['English']
        
        # Change Labels
        card_canvas.itemconfig(card_image, image=card_back_image)
        card_canvas.itemconfig(language_label, text="English", fill='black')
        card_canvas.itemconfig(word_label, text=f'{english}', fill='black')

        # global wrong_button_pressed
        # global right_button_pressed
        # wrong_button_pressed = False
        # right_button_pressed = False


# -------------------- USER INTERFACE -------------------- #
window = Tk()
window.title('Flashy Flashcard')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card_canvas.create_image(400, 263, image=card_front_image)
card_canvas.grid(column=0, row=1, columnspan=2)

# Labels
language_label = card_canvas.create_text(400, 50, text="Japanese", font=("Ariel", 20, "italic"))
word_label = card_canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))

# Buttons
wrong_button_image = PhotoImage(file='./images/wrong.png')
right_button_image = PhotoImage(file='./images/right.png')

wrong_button = Button(command=wrong_button, image=wrong_button_image, relief="flat", bg=BACKGROUND_COLOR,
                      highlightthickness=0)
wrong_button.grid(column=0, row=2)
right_button = Button(command=right_button, image=right_button_image, relief="flat", bg=BACKGROUND_COLOR,
                      highlightthickness=0)
right_button.grid(column=1, row=2)

# Init
random_card()

window.mainloop()
