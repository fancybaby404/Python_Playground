from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
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
def file_exists():
    try:
        with open(file='data.json', mode='r') as file:
            file.read()
        return True
    except FileNotFoundError:
        return False


def save():
    website = website_entry
    user_email = email_user_entry
    password = password_entry

    # Empty entries
    if len(website.get()) < 1 or len(user_email.get()) < 1 or len(password.get()) < 1:
        messagebox.showerror(title='Warning!', message='Please do not leave any of the entries empty.')
        return

    # pop-up: are you sure
    is_ok = messagebox.askokcancel(title=website.get(), message=f'These are the details entered:'
                                                                f'\n--------------------\n'
                                                                f'Email: {user_email.get()}\n'
                                                                f'Password: {password.get()}\n'
                                                                f'--------------------\n'
                                                                f'Are you okay with this?')

    # pop-up: are you sure = True
    if is_ok:
        new_data = {
            website.get().title(): {
                "email": user_email.get(),
                "password": password.get(),
            }
        }

        if not file_exists():
            # Create File if it doesn't exist
            with open(file='data.json', mode='w') as data_file:
                json.dump(new_data, data_file)
        else:
            # Read File
            with open(file='data.json', mode='r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
            # Update
            with open(file='data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)

        # Clear entries
        website.delete(0, END)
        user_email.delete(0, END)
        password.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #
def search_command():
    try:
        with open(file='data.json', mode='r') as data_file:
            data = json.load(data_file)
            website = data[website_entry.get().title()]
            messagebox.showinfo(title=website_entry.get().title(), message=f'Email: {website["email"]}\nPassword: {website["password"]}')
    except KeyError:
        messagebox.showerror(title='Error', message='No details for the website exists.')
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found.')


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
website_entry = Entry(width=26)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()

email_user_entry = Entry(width=45)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky='w')

password_entry = Entry(width=26)
password_entry.grid(column=1, row=3, columnspan=2, sticky='w')

# --------------- Buttons --------------- #
search_button = Button(command=search_command, text='           Search           ')
search_button.grid(column=1, row=1, columnspan=2, sticky='e')

generate_button = Button(command=generate_password, text='Generate Password')
generate_button.grid(column=1, row=3, columnspan=2, sticky='e')

add_button = Button(command=save, text='Add', width=38)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
