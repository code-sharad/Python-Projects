# currency
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
Pennies = 0.01

MENU = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "price": 2.50,

    },
    'espresso': {
        "ingredients": {
            "water": 50,
            "coffee": 18},
        "price": 1.50,

    }
    ,
    'cappuccino': {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24},
        "price": 2.50}
}
profit = 0

resources = {
    "coffee": 100,
    "water": 300,
    "milk": 200
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough water.")
            return False
    return True


def process_coins():
    print("Please insert coin.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    print(total)
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Coffee {resources['coffee']}g.")
        print(f"Water {resources['water']}ml.")
        print(f"Milk {resources['milk']}ml.")
        print(f"Money ${profit}.")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["price"]):
                make_coffee(choice, drink["ingredients"])

    # flavours

    # if choice == 'latte':
    #     choose = 'LATTE'
    #     num = 'LATTE'
    #
    # elif choice == 'espresso':
    #     choose = MENU[0]['NAME']
    #     num = 'ESPRESSO'
    #
    # elif choice == 'pennies':
    #     choose = Pennies
    #     num = 'CAPPUCCINO'
    #
    # if choice == 'off':
    #     turn_on = False

    #
    # def coffee_machine(Water=MENU[num]['WATER'], Milk=MENU[num]['Milk'], Coffee=MENU[num]['NAME'], MONEY=MONEY):
    #
    #
    #
    #     print("Please insert coins.")
    #     quarters = int(input("How many quarters?: "))
    #     dimes = int(input("How many dimes?: "))
    #     nickles = int(input("How many nickles?: "))
    #     pennies = int(input("How many pennies?: "))
    #     total_money = ((QUARTERS * quarters) + (DIMES * dimes) + (nickles * NICKLES) + (Pennies * pennies))
    #
    #     Water -= MENU[num]['WATER']
    #     if WATER < MENU[num]['WATER']:
    #         print("Sorry their is not enough water.")
    #
    #     elif total_money < MENU[num]['PRICE']:
    #         MONEY -= total_money
    #         print("Sorry that's not enough money. Money refunded")
    #     elif total_money > MENU[num]['PRICE']:
    #         MONEY += MENU[num]['PRICE']
    #         print(f"Here is ${total_money - MENU[num]['PRICE']} in change.")
    #         print(f"Here is your little {choice} enjoy!")
    #
    #
    # coffee_machine()
