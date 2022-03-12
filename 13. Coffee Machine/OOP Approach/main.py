from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# OOP Approach : A cleaner way

def coffee():
    """ Starts the coffee machine"""
    machine_on = True
    make_coffee = CoffeeMaker()
    money_thing = MoneyMachine()
    menu = Menu()
    while machine_on:
        # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
        print("Welcome to our Caffe, here's the menu")
        choice = input(
            f"Espresso: ₹80\nLatte: ₹200\nCappuccino: ₹300\nWhat would you like? {menu.get_items()}:\n").lower()
        if choice == "off":
            machine_on = False
            print("Thanks for using me, come back soon!")
        # TODO 3: Print report.
        elif choice == "report":
            make_coffee.report()
            money_thing.report()
        else:
            if menu.find_drink(choice) is None:
                print("Please enter a valid choice 😡💢\n")
            else:
                drink = menu.find_drink(choice)
                if make_coffee.is_resource_sufficient(drink) and money_thing.make_payment(drink.cost):
                    make_coffee.make_coffee(drink)


coffee()
