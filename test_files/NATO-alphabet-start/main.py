import pandas

# TODO 1. Create a dictionary in this format:
# {'A': 'Alpha', 'B': 'Bravo'}
raw_nato_dict = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in raw_nato_dict.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = list(input('Enter a word: ').upper())

new_user_word = [nato_dict[word] for word in user_word]
print(new_user_word)
