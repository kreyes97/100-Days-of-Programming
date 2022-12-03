from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def make_coffee(user_input):
    coffee_obj = menu.find_drink(user_input)
    can_make = coffee_maker.is_resource_sufficient(coffee_obj)
    if can_make == False:
        return False
    else:
        money_check = money_machine.make_payment(coffee_obj.cost)
        if money_check == False:
            return False
        else:
            coffee_maker.make_coffee(coffee_obj)


def main():
    global coffee_maker, money_machine, menu
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        coffee_types = ["latte", "cappuccino", "espresso"]
        user_input = input(f"What would you like? {menu.get_items()}: ")
        if user_input == "off":
            print("Turning off...")
            break
        elif user_input in coffee_types:
            make_coffee(user_input)
            continue
        elif user_input == "report":
            money_machine.report()
            coffee_maker.report()
            continue
        else:
            print("Invalid input.")
            continue


main()
