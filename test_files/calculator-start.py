#Calculator
from art import logo

def add(n1, n2):
	result = n1 + n2
	return result
def subtract(n1, n2):
	result = n1 - n2
	return result
def multiply(n1, n2):
	result = n1 * n2
	return result
def divide(n1, n2):
	result = n1 / n2
	return result

operations = {
	"+":add,
	"-":subtract,
	"*":multiply,
	"/":divide,
}

def calculator():
	print(logo)
	num1 = float(input("What's the first number?: "))

	for operators in operations:
		print(operators)

	operation_symbol = input("Pick an operation from the line above: ")

	num2 = float(input("What's the second number?: "))

	calculation_function = operations[operation_symbol]
	first_answer = calculation_function (num1, num2)
	print(f"{num1} {operation_symbol} {num2} = {first_answer}")

	continue_calc = True
	while(continue_calc):
		continue_calc = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit: ")
		
		if continue_calc == 'n':
			return False

		operation_symbol = input("Pick an operation: ")
		num3 = float(input("What's the next number?: "))
		calculation_function = operations[operation_symbol]
		second_answer = calculation_function(first_answer, num3)
		print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
		first_answer = second_answer

calculator()