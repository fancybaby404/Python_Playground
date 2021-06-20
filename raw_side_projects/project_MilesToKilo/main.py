from tkinter import Tk, Entry, Label, Button, END

FONT = ("Arial", 10, "normal")

# --------------- Functions ---------------
def miles_to_km():
    conversion_factor = 0.62137119
    if type(miles_input.get()) is int:
        return int(miles_input.get()) / conversion_factor
    else:
        return float(miles_input.get()) / conversion_factor
def button_pressed():
    converted_km.config(text=f'{round(miles_to_km(), 2)}')

# --------------- Initialization ---------------

# window
window = Tk()
window.configure(bg='black')
window.title("Miles To Kilometers")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)
window.resizable(False, False)

# row 0
miles_input = Entry(width=10, justify='center', font=FONT)
miles_input.insert(END, 0)
miles_input.grid(column=1, row=0)
miles_input.configure(bg='black')
miles_input.configure(fg='white')

m_text = Label(text='Miles', font=FONT)
m_text.grid(column=3, row=0)
m_text.configure(bg='black')
m_text.configure(fg='white')

# row 1
eq_text = Label(text='is equal to', font=FONT)
eq_text.grid(column=0, row=1)
eq_text.config(padx=10, pady=10)
eq_text.configure(bg='black')
eq_text.configure(fg='white')

converted_km = Label(width=10, text='0', font=FONT)
converted_km.grid(column=1, row=1)
converted_km.configure(bg='black')
converted_km.configure(fg='white')

k_text = Label(width=10, text='Km')
k_text.grid(column=3, row=1)
k_text.configure(bg='black')
k_text.configure(fg='white')

# row 2
calc_button = Button(text='Calculate', command=button_pressed)
calc_button.grid(column=1, row=2)
calc_button.configure(bg='black')
calc_button.configure(fg='white')

window.mainloop()
