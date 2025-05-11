# Define the MENU dictionary with correct indentation
MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
            "coffee": 80,
            "water": 100,
        },
        "cost": 1.50,
    },
    "cappuccino": {
        "ingredients": {
            "milk": 0,
            "coffee": 80,
            "water": 100,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "milk": 0,
            "coffee": 80,
            "water": 100,
        },
        "cost": 1.50,
    },
}

# Initialize profit and resources
profit = 0
resources = {
    "milk": 300,
    "water": 300,
    "coffee": 300,
}

# Function to check if resources are sufficient
def is_resource_sufficient(order_ingredients):
    """returns True when order can be made, and False when ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function to process coins
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total  # Return the total amount

# Function to check if transaction is successful
def is_transaction_successful(money_received, drink_cost):
    """return True when money is excepted, or False if money is insufficient"""
    if money_received >= drink_cost:  # Changed to >= to allow for exact payment
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost  # Corrected the operator
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Main loop
is_on = True
while is_on:
    choice = input("What would you like ('espresso', 'cappuccino', or 'latte'): ").lower()

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Water: {resources['water']}ml")
        print(f"Money: ${profit}")
    elif choice in MENU:  # Check if choice is a valid drink
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                # Deduct ingredients from resources
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]
                print(f"Here is your {choice}. Enjoy!")
    else:
        print("Invalid choice. Please try again.")








