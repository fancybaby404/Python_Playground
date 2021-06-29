from tkinter import *
import pandas as pd
from random import randint
import cutlet
from jamdict import Jamdict

# GLOBALS
BACKGROUND_COLOR = "#B1DDC6"
rand_index = 0

# ------------------- DOESNT work right off ------------------- #
# You have to change the indices | Japanese -> 1 | English -> 2 |
jp_words_DATA = pd.read_csv('data/japanese_words.json')

# EXPERIMENT
jp2_words_DATA = pd.read_csv('data/japanese_words.json')

# ------------------- WILL work right off ------------------- #
hiragana_DATA = pd.read_csv('./data/hiragana_letters.csv')
katakana_DATA = pd.read_csv('./data/katakana_letters.csv')

jam = Jamdict()


def remove_chars(result):
    chars_to_remove = "[]:"
    num = ('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '0.')
    for char in chars_to_remove:
        result = str(result).replace(char, ' ')
    for char in num:
        result = result.replace(char, ' ')
    return result.strip().split()


# -------------------- READING DATA -------------------- #
def random_card():
    global rand_index
    global jp_words_DATA

    rand_index = randint(0, 44)
    data_list = jp2_words_DATA.loc[rand_index].tolist()

    result = jam.lookup(data_list[0]).entries
    new_result = remove_chars(result)

    card_canvas.itemconfig(language_label, text="Hiragana", fill='black')
    card_canvas.itemconfig(word_label, text=f'{new_result[0]}\n{new_result[1]}', fill='black')
    card_canvas.itemconfig(card_image, image=card_front_image)

    window.after(5000, flip_card)


# -------------------- FLIP CARD -------------------- #
def flip_card():
    stop = 'abcdefghijklmnopqrstuvwxyz1234567890.'
    global rand_index
    global jp_words_DATA
    added_newline = False
    data_list = jp2_words_DATA.loc[rand_index].tolist()

    result = jam.lookup(data_list[0]).entries
    removed_chars = remove_chars(result)
    new_result = []
    for char in removed_chars[2:]:
        if stop in char:
            pass
        else:
            if len(new_result) > 3 and not added_newline:
                char += '\n'
                added_newline = True
            new_result.append(char)

    card_canvas.itemconfig(card_image, image=card_back_image)
    card_canvas.itemconfig(language_label, text="Romaji", fill='white')
    card_canvas.itemconfig(word_label, text=f'{" ".join(new_result)}', fill='white')


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
language_label = card_canvas.create_text(400, 50, text="Japanese", font=("Ariel", 10, "italic"))
word_label = card_canvas.create_text(400, 263, text="Word", font=("Ariel", 20, "bold"))

# Buttons
wrong_button_image = PhotoImage(file='./images/wrong.png')
right_button_image = PhotoImage(file='./images/right.png')

wrong_button = Button(command=random_card, image=wrong_button_image, relief="flat", bg=BACKGROUND_COLOR,
                      highlightthickness=0)
wrong_button.grid(column=0, row=2)
right_button = Button(command=random_card, image=right_button_image, relief="flat", bg=BACKGROUND_COLOR,
                      highlightthickness=0)
right_button.grid(column=1, row=2)

# Init
random_card()

window.mainloop()
