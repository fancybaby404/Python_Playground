from random import choice
import smtplib
import datetime as dt
import pandas as pd
def clear_terminal():
    import os
    os.system('cls')
clear_terminal()

list_of_birthdays = pd.read_csv('birthdays.csv')

column_month = list_of_birthdays['month'].values
column_day = list_of_birthdays['day'].values

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

letter_templates = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
if current_month in column_month and current_day in column_day:
    # Converting the whole column_month into a list, allows me to use the index() to find the
    # index of the current_month in the list.
    index = list(column_month).index(current_month)
    data = list_of_birthdays.iloc[index]

    birthday_name = data['name']
    birthday_email = data['email']
    with open(file=f'./letter_templates/{choice(letter_templates)}', mode='r') as letter:
        letter_data = letter.read()
        letter_data = letter_data.replace('[NAME]', birthday_name)

    my_email = ''
    password = ''
    PORT = 587
    with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f'Subject:Happy Birthday! :))\n\n{letter_data}'
        )
        print(f'Birthday message sent to: {birthday_name}')
