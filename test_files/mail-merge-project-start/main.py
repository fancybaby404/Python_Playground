from os.path import dirname, join
current_dir = dirname(__file__)

invited_names = join(current_dir, "./Input/Names/invited_names.txt")
starting_letter = join(current_dir, "./Input/Letters/starting_letter.txt")

# Gets all the names in the invited_names.txt and puts it into a variable.
# With the functions .read() it gets the contents of the file and .splitlines() removes the \n
with open(invited_names) as invited_names:
    list_name_no_space = invited_names.read().splitlines()

# First we put the contents in the starting letter into a variable using read(),
with open(starting_letter) as letter_content:
    letter = letter_content.read()
    # now we make a for loop saying, for each name in the list of names we created ^above,
    # we get the letter contents and use the method .replace() getting the "[name]" and replacing
    # that with each of the name in the list. This is entered in the new variable called 'new_name'
    for name in list_name_no_space:
        final_letter = join(current_dir, (f"./Output/ReadyToSend/letter_for_{name}.txt"))
        new_letter = letter.replace("[name]", name)
        # We then create files by using the mode="a" (append), for each name in the list,
        # we make a new letter using the newly created new_letter with the replaced name.
        with open(final_letter, mode="a") as letters:
            letters.write(new_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
