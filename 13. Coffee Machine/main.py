MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 80,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
not_available = []


# TODO 2: Check resources sufficient?
def is_resource_sufficient(ingredients, choice):
    """ Check and returns true if resource to make an order are sufficient otherwise returns false """
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there's is not enough {item}.\n")
            if choice not in not_available:
                not_available.append(choice)
            return False
    return True


# TODO 4: Process coins
def currency_processor():
    """Returns the total calculated from  inserted."""
    print("\nPlease insert money(only INR accepted; in cash only)")
    total = int(input("how many ₹1 currency: "))
    total += int(input("how many ₹2 currency: ")) * 2
    total += int(input("how many ₹5 currency: ")) * 5
    total += int(input("how many ₹10 currency: ")) * 10
    total += int(input("how many ₹20 currency: ")) * 20
    total += int(input("how many ₹50 currency: ")) * 50
    total += int(input("how many ₹100 currency: ")) * 100
    total += int(input("how many ₹200 currency: ")) * 200
    total += int(input("how many ₹500 currency: ")) * 500
    total += int(input("how many ₹2000 currency: ")) * 2000
    return total


# TODO 5: Check transaction successful?
def is_payment_success(payment_received, cost):
    """ Checks if payment_received is enough, if sufficient returns the change and true; if not, it returns the
    payment """
    if payment_received >= cost:
        change = round(payment_received - cost)
        if change != 0:
            print(f"\nHere is ₹{change} in change.")
        global profit
        profit += cost
        return True
    else:
        return False


# TODO 6: Finally make user's choice
def make_coffee(choice, ingredients):
    """ Makes coffee and deducts the resources used"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕️Enjoy!\n")


def coffee():
    """ Starts the coffee machine"""
    machine_on = True
    while machine_on:
        # TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
        print("Welcome to our Caffe, here's the menu")
        choice = input("Espresso: ₹80\nLatte: ₹200\nCappuccino: ₹300\nWhat would you like? ("
                       "espresso/latte/cappuccino):\n").lower()
        if choice == "off":
            machine_on = False
            print("Thanks for using me, come back soon!")
        # TODO 3: Print report.
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
            print(f"Money: ${profit}")
        else:
            if choice not in MENU:
                print("Please enter a valid choice 😡💢\n")
            else:
                drink = MENU[choice]
                if is_resource_sufficient(drink["ingredients"], choice):
                    payment_received = currency_processor()
                    if is_payment_success(payment_received, drink["cost"]):
                        make_coffee(choice, drink["ingredients"])
                    else:
                        print("Sorry, that's not enough money. Money refunded :(\n")
                if len(not_available) > 1:
                    print("Sorry, we're not available, undergoing maintenance...resources not sufficient...Shutting "
                          "down 📴 ")
                    machine_on = False


coffee()
