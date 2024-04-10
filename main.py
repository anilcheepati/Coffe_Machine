MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resource={
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money=0

def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry there is no enough ingredients {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")

    quater = round(float(0.25 * int(input("How many Quaters? "))), 2)
    dimes = round(float(0.10 * int(input("How many dimes? "))), 2)
    nickels = round(float(0.05 * int(input("How many nickels? "))), 2)
    penny = round(float(0.01 * int(input("How many penny's? "))), 2)
    total = round(quater + dimes + nickels + penny, 2)
    return total


def transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change=round(money_received-drink_cost, 2)
        print(f"Here is your change = {change}")
        global money
        money+=drink_cost
        return True
    else:
        print("Sorry that not enough money to buy it . Money refunded !")
        return False



def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resource[item]-=order_ingredients[item]
    print(f"Here is your drink {drink_name}")




is_machine_on = True
while is_machine_on:
    type_of_coffe=input("What would you like ? ")
    if type_of_coffe == "off":
        is_machine_on=False
    elif type_of_coffe== "report":
        print(f"water ={resource['water']}ml")
        print(f"milk = {resource['milk']}ml")
        print(f"coffe = {resource['coffee']}gm")
        print(f"money=${money}")
    else:
        drink=MENU[type_of_coffe]
        print(drink)
        if resources_sufficient(drink["ingredients"]):
            payment=process_coins()
            print(payment)
            if transaction_successful(payment,drink['cost']):
                make_coffee(type_of_coffe,drink["ingredients"])










