from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for _ in range(randint(8, 10))]

    [password_list.append(choice(symbols)) for _ in range(randint(2, 4))]

    [password_list.append(choice(numbers)) for _ in range(randint(2, 4))]

    shuffle(password_list)

    random_password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry
    user_email = email_user_entry
    password = password_entry

    if len(website.get()) < 1 or len(user_email.get()) < 1 or len(password.get()) < 1:
        messagebox.showerror(title='Warning!', message='Please do not leave any of the entries empty.')
        return

    is_ok = messagebox.askokcancel(title=website.get(), message=f'These are the details entered:'
                                                                f'\n--------------------\n'
                                                                f'Email: {user_email.get()}\n'
                                                                f'Password: {password.get()}\n'
                                                                f'--------------------\n'
                                                                f'Are you okay with this?')

    if is_ok:
        with open(file='data.txt', mode='a') as txt:
            final_text = f'{website.get()} | {user_email.get()} | {password.get()}\n'
            txt.write(final_text)

        # Clear entries
        website.delete(0, END)
        user_email.delete(0, END)
        password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# --------------- Logo --------------- #
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# --------------- Labels --------------- #
website_label = Label(text='Website:')
website_label.grid(column=0, row=1, sticky='e')

email_user_label = Label(text='Email/Username:')
email_user_label.grid(column=0, row=2, sticky='e')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3, sticky='e')

# --------------- Entries --------------- #
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()

email_user_entry = Entry(width=45)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky='w')

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, columnspan=2, sticky='w')

# --------------- Buttons --------------- #
generate_button = Button(command=generate_password, text='Generate Password')
generate_button.grid(column=1, row=3, columnspan=2, sticky='e')

add_button = Button(command=save, text='Add', width=38)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
