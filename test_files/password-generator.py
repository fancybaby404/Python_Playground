#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_password = ""

for random_letter in range(0,nr_letters):
    rand_letters = random.choice(letters)
    random_password += rand_letters
for random_symbols in range(0,nr_symbols):
    rand_symbols = random.choice(symbols)
    random_password += rand_symbols
for random_numbers in range(0,nr_numbers):
    rand_numbers = random.choice(numbers)
    random_password += rand_numbers
    

char_list = list(random_password)
random.shuffle(char_list)
final_str = ''.join(char_list)
print(f"Your random password:\n {final_str}")
