from tkinter import *
import math
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
TEXT_COLOR = "#406B82"
BG_COLOR = "#F5F5F5"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = []
timer = None
pause_called = False
current_time = 0
flag = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global pause_called
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if not pause_called:
        reps += 1

    if reps % 8 == 0:
        if not pause_called:
            play_music()
        count_down(long_break)
        timer_text.config(text='Long', fg=RED)
    if reps % 2 == 0:
        # Pink
        if not pause_called:
            play_music()
        timer_text.config(text='Break', fg=PINK)
        count_down(short_break)
    if reps % 2 != 0:
        if reps == 1:
            pass
        elif not pause_called:
            play_music()
        # Green
        timer_text.config(text='Work', fg=TEXT_COLOR)
        count_down(work_time)
    pause_called = False


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Get minutes from seconds: SECONDS / 60
# Get remaining seconds: SECONDS % 60

def count_down(count):
    global timer
    global current_time
    global pause_called

    count_min = math.floor(count / 60)
    count_sec = count % 60

    new_count_min = math.floor(current_time / 60)
    new_count_sec = current_time % 60

    # Normal
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f'0{int(count_sec)}'

    # Pause
    if new_count_sec == 0:
        new_count_sec = "00"
    elif new_count_sec < 10:
        new_count_sec = f'0{int(new_count_sec)}'

    if not pause_called:
        canvas.itemconfig(pomodoro_timer, text=f'{count_min}:{count_sec}')
    elif pause_called:
        canvas.itemconfig(pomodoro_timer, text=f'{new_count_min}:{new_count_sec}')

    if count > 0:
        if not pause_called:
            timer = window.after(1000, count_down, count - 1)

        if pause_called:
            timer = window.after(1000, count_down, current_time - 1)
        current_time = count
    else:
        for num in range(1, 9, 2):
            if reps == num:
                marks.append("✅")
                check_mark.config(text=marks)
        start_timer()
    pause_called = False


# ---------------------------- PLAY BUTTON ------------------------------- #
def play():
    global flag
    global pause_called

    button_sound()
    if flag == 0:
        start_timer()
    elif flag != 0 and pause_called:
        start_timer()
    flag += 1


# ---------------------------- PAUSE BUTTON ------------------------------- #

def pause():
    button_sound()
    try:
        global pause_called
        pause_called = True
        window.after_cancel(timer)
    except Exception:
        pass


# ---------------------------- TIMER RESET BUTTON ------------------------------- #

def reset_timer():
    try:
        global reps
        global marks
        global pause_called
        global current_time
        global flag

        flag = 0
        reps = 0
        marks = []
        pause_called = False
        current_time = 0

        button_sound()
        check_mark.config(text=marks)
        window.after_cancel(timer)
        canvas.itemconfig(pomodoro_timer, text=f'00:00')
        timer_text.config(text="Timer", fg=TEXT_COLOR)
    except Exception:
        pass


# ---------------------------- SOUNDS ------------------------------- #
pygame.mixer.init()


def play_music():
    pygame.mixer.music.load("alarm.wav")
    pygame.mixer.music.play(loops=0)


def button_sound():
    pygame.mixer.music.load("button_click.mp3")
    pygame.mixer.music.play(loops=0)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.resizable(False, False)
window.title('Pomodoro Timer')
window.config(padx=25, bg=BG_COLOR)
canvas = Canvas(width=204, height=224, bg=BG_COLOR, highlightthickness=0)

# Tomato Image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

# Pomodoro Timer
pomodoro_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Timer Label
timer_text = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
timer_text.grid(column=1, row=0)

# Pause Button
pause_image = PhotoImage(file='pause_button.png').subsample(10)
pause_button = Button(command=pause, relief="flat", image=pause_image, bg=BG_COLOR)
pause_button.grid(column=0, row=2)

# Play Button
play_image = PhotoImage(file='play_button.png').subsample(10)
play_button = Button(command=play, relief="flat", image=play_image, bg=BG_COLOR)
play_button.grid(column=1, row=2)

# Reset Button
reset_image = PhotoImage(file='reset_button.png').subsample(10)
reset_button = Button(command=reset_timer, relief="flat", image=reset_image, bg=BG_COLOR)
reset_button.grid(column=2, row=2)

# Check Mark
check_mark = Label(fg=TEXT_COLOR, bg=BG_COLOR)
check_mark.config(padx=20, pady=20)
check_mark.grid(column=1, row=3)

window.mainloop()
