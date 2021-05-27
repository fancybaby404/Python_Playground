from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiate
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Grab drink names
drinks = Menu().get_items()

# ---- Start of Loop ----
is_on = True
while is_on:
    # What would you like? (espresso/latte/cappuccino):
    choice = input(f"What would you like? {drinks}: ")

    # on and off:
    if choice == 'off':
        exit()

    # Report machine resources
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
        continue

    # get price/name/ingredients of drink
    try:
        drink_choice = menu.find_drink(choice)

        # Check if machine resources are sufficient
        if coffee_maker.is_resource_sufficient(drink_choice):
            if money_machine.make_payment(drink_choice.cost):
                coffee_maker.make_coffee(drink_choice)
                continue
        else:
            print(f"Resources are not sufficient to make {choice}")
            continue
    except Exception:
        continue
