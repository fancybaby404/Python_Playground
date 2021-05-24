from art import logo,vs
import os
from game_data import data
from random import randint


# ----- Functions -----
def screen_clear():
    os.system('cls')

def play_again():
	play_again = input("Do you want to play another game? Type 'y' or 'n': ")
	if play_again == 'y':
		screen_clear()
		higher_lower()
	elif play_again == 'n':
		return

def get_info(index):
	name = data[index]["name"]
	description = data[index]["description"]
	country = data[index]["country"]
	return f"{name}, a {description}, from {country}"

def compare(index1,index2):
	"""Returns the index of who has more follower_count"""
	index1_follower_count = data[index1]["follower_count"] #A
	index2_follower_count = data[index2]["follower_count"] #B

	if int(index1_follower_count) > int(index2_follower_count):
		return index1
	elif int(index2_follower_count > int(index1_follower_count)):
		return index2

# ----- Main -----

def higher_lower():
	random_index = randint(0,len(data) - 1)
	score = 0
	game_over = False
	greater_follower_index = 0

	# ----- Display -----
	while game_over == False:
		screen_clear()
		print(logo)
		random_index = randint(0,len(data) - 1)
		# Makes the compare A the winning letter (remove it if unwated)
		if greater_follower_index != 0:
			random_index = greater_follower_index
		print(f"Compare A: {get_info(random_index)}")
		first_index = random_index # stores the index for comparation
		
		print(f"\n{vs}\n")
		# Checks if the random_index is the same as the first one
		# if it is, then change it randomizes a random index again
		while random_index == first_index:
			if random_index == random_index:
				random_index = randint(0,len(data) - 1)
		print(f"Compare B: {get_info(random_index)}")
		second_index = random_index # stores the index for comparation
		# ----- End of Display -----

		# ----- Input -----
		guess = input("Who has more followers 'A' or 'B': ").lower()
		greater_follower_index = compare(first_index, second_index) # returns the index of > flwr_count


		# Finds the greater follower index and sets a new variable to the winning letter, if first index is greater then 'A' if second index is greater then 'B'.
		winning_letter = ''
		if str(greater_follower_index) == str(first_index):
			winning_letter = 'a'
		elif str(greater_follower_index) == str(second_index):
			winning_letter = 'b'
		
		#print(f"Winning Letter: {winning_letter}")
		# ----- Get Score or Lose -----
		if guess == winning_letter:
			screen_clear()
			score += 1
			print(f"\nYou're right! Current score: {score}")
		else:
			game_over = True
			print(f"Sorry that's wrong!\nFinal Score: {score}")
			play_again()

# ----- End of Main -----
higher_lower()