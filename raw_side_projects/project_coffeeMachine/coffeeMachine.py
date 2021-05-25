from report import MENU, resources
from art import coffee_art, machine_art, cafe_menu
from os import system
from time import sleep


# ---------- FUNCTIONS ----------

def screen_clear():
    system('cls')


def get_coffee_cost(user_choice):
    """Returns the price of the coffee in the report dictionary based on the user choice"""
    return MENU[user_choice]["cost"]


def report(machine_money, water, milk, coffee):
    """Returns a report of the coffee machine resources, parameter is the machine's current money"""
    return f"    Water: {water}\n    Milk: {milk}\n    Coffee: {coffee}\n    Money: ${machine_money}"


def sufficient_resources(user_choice, water, milk, coffee):
    """Returns true if the resources of the coffee machine are sufficient, false otherwise."""
    # checks the resources if it can make the coffee
    if user_choice == 'espresso':
        if water > 50 and coffee > 18:
            return True
        else:
            return False
    if user_choice == 'latte':
        if water > 200 and milk > 150 and coffee > 24:
            return True
        else:
            return False
    if user_choice == 'cappuccino':
        if water > 250 and milk > 100 and coffee > 24:
            return True
        else:
            return False


def coin_mechanism(coffee_price, user_quarter, user_dime, user_nickel, user_penny):
    """Deducts the coffee price by the money, if coffee_price is <= 0
    it will return a change in a absolute value. Else if the coffee_price
     is not > 0 then it will return false."""
    coffee_price -= user_quarter
    coffee_price -= user_dime
    coffee_price -= user_nickel
    coffee_price -= user_penny

    if coffee_price <= 0:
        return abs(coffee_price)
    elif coffee_price > 0:
        return False


def minus_resources(user_choice, water, milk, coffee):
    water -= int(MENU[user_choice]["ingredients"]["water"])
    milk -= int(MENU[user_choice]["ingredients"]["milk"])
    coffee -= int(MENU[user_choice]["ingredients"]["coffee"])
    return water, milk, coffee


def refill_resources(water, milk, coffee):
    water += 300
    milk += 250
    coffee += 100
    return water, milk, coffee


# ---------- MAIN ----------
def coffee_machine():
    machine_money = 0
    resources_water = resources["water"]
    resources_milk = resources["milk"]
    resources_coffee = resources["coffee"]

    end_coffee_machine = False
    while not end_coffee_machine:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Refills the resources for the coffee machine
        if user_choice == 'refill':
            resources_water, resources_milk, resources_coffee = refill_resources(resources_water, resources_milk,
                                                                                 resources_coffee)
            print("    Successfully refilled the machine.")
            continue

        # Gives information for the resources of the coffee machine
        if user_choice == 'report':
            print(report(machine_money, resources_water, resources_milk, resources_coffee))
            continue

        # Gives information about the menu of the coffee machine
        if user_choice == 'menu':
            print(cafe_menu)
            print(f"    Latte: ${latte_cost}\n    Espresso: ${espresso_cost}\n    Cappuccino: ${cappuccino_cost}")
            continue

        # Checks if the user_choice is in the menu
        if user_choice not in MENU:
            print("    Invalid Order.")
            continue

        coffee_price = get_coffee_cost(user_choice)

        # Checks if the machine resources are enough
        sufficient_resources(user_choice, resources_water, resources_milk, resources_coffee)
        if not sufficient_resources(user_choice, resources_water, resources_milk, resources_coffee):
            print(f"    There is not enough resources to make {user_choice}")
            continue

        # Coin Mechanism
        print("Please insert coins.")
        try:
            user_quarter = int(input("    how many quarters?: ")) * QUARTER
            user_dime = int(input("    how many dime?: ")) * DIME
            user_nickel = int(input("    how many nickel?: ")) * NICKEL
            user_penny = int(input("    how many penny?: ")) * PENNY
        except Exception:
            # Checks if the user did not input a non numeric input
            print("    Invalid input")
            continue
        print("Money recieved...\nCalculating...")
        sleep(3)
        # <1> Deducts the price of the coffee by the money given, returns false if not enough,
        if not coin_mechanism(coffee_price, user_quarter, user_dime, user_nickel, user_penny):
            print("    Sorry that's not enough money. Money refunded.")
            continue
        #  <2> returns the absolute value negative(change) if successful.
        if coin_mechanism:
            screen_clear()
            print(machine_art)
            print(f"Please wait...\nMaking {user_choice}...")
            sleep(6)
            resources_water, resources_milk, resources_coffee = minus_resources(user_choice, resources_water,
                                                                                resources_milk, resources_coffee)
            machine_money += coffee_price
            print(
                f"Here is {coin_mechanism(coffee_price, user_quarter, user_dime, user_nickel, user_penny)} in change.")
            print(f"Here is your {user_choice} enjoy!")
            print(coffee_art)
            sleep(6)
            screen_clear()
            continue


# ---------- END OF MAIN ----------


# ---------- INITIALIZATION ----------


PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]

coffee_machine()
