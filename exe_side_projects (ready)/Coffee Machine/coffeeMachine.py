from report import MENU, resources


# ---------- FUNCTIONS ----------

def get_coffee_cost(coffee):
    if coffee == 'espresso':
        return MENU["espresso"]["cost"]
    if coffee == 'latte':
        return MENU["latte"]["cost"]
    if coffee == 'cappuccino':
        return MENU["cappuccino"]["cost"]


def report(machine_money):
    """Returns a report of the coffee machine resources, parameter is the machine's current money"""
    return f"    Water: {resources_water}\n    Milk: {resources_milk}\n    Coffee: {resources_coffee}\n    Money: ${machine_money}"


def sufficient_resources(coffee, boolean):
    """Returns true if the resources of the coffee machine are sufficient, false otherwise."""
    # checks the resources if it can make the coffee
    if coffee == 'espresso':
        if resources_water > 50 or resources_coffee > 18:
            return boolean == True
        else:
            boolean == False
    if coffee == 'latte':
        if resources_water > 200 or resources_milk > 150 or resources_coffee > 24:
            return boolean == True
        else:
            return boolean == False
    if coffee == 'cappuccino':
        if resources_water > 250 or resources_milk > 100 or resources_coffee > 24:
            return boolean == True
        else:
            return boolean == False


def coin_mechanism(coffee_price, user_quarter, user_dime, user_nickel, user_penny, machine_money):
    stored_money = coffee_price
    coffee_price -= user_quarter
    coffee_price -= user_dime
    coffee_price -= user_nickel
    coffee_price -= user_penny

    if coffee_price <= 0:
        return abs(coffee_price)
    elif coffee_price > 0:
        return False


# ---------- MAIN ----------
def coffee_machine():
    machine_money = 0

    end_coffee_machine = False
    while not end_coffee_machine:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_choice == 'report':
            print(report(machine_money))
            continue

        # Checks if the user_choice is in the menu
        if user_choice not in MENU:
            print("    Invalid Order.")
            continue

        coffee_price = get_coffee_cost(user_choice)

        # Checks if the machine resources are enough
        is_sufficient = True
        sufficient_resources(user_choice, is_sufficient)
        if not sufficient_resources(user_choice, is_sufficient):
            print(f"    There is not enough resources to make {user_choice}")
            continue

        # Coin Mechanism
        print("Please insert coins.")
        try:
            user_quarter = int(input("how many quarters?: ")) * QUARTER
            user_dime = int(input("how many dime?: ")) * DIME
            user_nickel = int(input("how many nickel?: ")) * NICKEL
            user_penny = int(input("how many penny?: ")) * PENNY
        except Exception:
            print("    Invalid input")
            continue

        if not coin_mechanism(coffee_price, user_quarter, user_dime, user_nickel, user_penny, machine_money):
            print("    Sorry that's not enough money. Money refunded.")
            continue
        if coin_mechanism:
            machine_money += coffee_price
            print(f"Here is {coin_mechanism(coffee_price, user_quarter, user_dime, user_nickel, user_penny, machine_money)} in change.")
            print(f"Here is your {user_choice} enjoy! ☕")
            continue


# ---------- END OF MAIN ----------


# ---------- INITIALIZATION ----------


PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

resources_water = resources["water"]
resources_milk = resources["milk"]
resources_coffee = resources["coffee"]

espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]

coffee_machine()

# DONE: 1. Ability to print the 'report' which is the contents of the machine (milk, water,
# DONE: 2. Check if the resources are sufficient
# DONE: 3. Process the coins
# DONE: 4. Check if transaction successful
# DONE: 5. Make the coffee
