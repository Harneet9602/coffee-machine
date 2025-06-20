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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit=0
coffee_machine_on= True

def sufficient_resources(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry! There is not enough {item}")
            is_enough= False
    return is_enough

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_successful(money_entered, drink_cost):
    if money_entered>=drink_cost:
        change = round(money_entered-drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"Here is your {drink_name}")

while coffee_machine_on:
    coffee=input("What would you like to have?(espresso/latte/cappuccino): ").lower()
    if coffee == 'off':
        print("Turning off in  3..2..1.")
        coffee_machine_on = False
    elif coffee=='report':
        print("We have these resources left:")
        for i in resources:
            if i == "coffee":
                print(f"{i}: {resources[i]} g")
            else:
                print(f"{i}: {resources[i]} ml")
        print(f"Money: {profit}")
    else:
        drink = MENU[coffee]
        if sufficient_resources(drink['ingredients']):
            payment=round(process_coins(),2)
            print(f"Your total is: ${payment}")
            if transaction_successful(payment,drink['cost']):
                make_coffee(coffee,drink['ingredients'])
            else:
                print("Transaction not successful")
        else:
            print("Resources not sufficient")
