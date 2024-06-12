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
    "money": 0
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def coffee_chose():
    chose = True
    while chose:
        coffee_type = input("What would you like? (espresso/latte/cappuccino)").lower()
        if coffee_type == "report":
            report()
        else:
            chose = False
            return coffee_type


def user_money():
    all_money = int(input("how many quarters?:"))*0.01
    all_money += int(input("how many dimes?:"))*0.10
    all_money += int(input("how many nickles?:"))*0.05
    all_money += int(input("how many pennies?:"))*0.25
    return all_money


def remorse_check(coffee):
    coffee_type = MENU[coffee]["ingredients"]
    for item in coffee_type:
        if coffee_type[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def order(coffee):
    coffee_type = MENU[coffee]["ingredients"]
    money = user_money()
    cost = MENU[coffee]["cost"]
    if money > cost:
        resources["money"] += cost
        for item in coffee_type:
            resources[item] -= coffee_type[item]
        print(f"Here is {round(money-cost, 2)}$ in change.")
        print(f"Here is your {coffee} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


run = True
while run:
    coffee = coffee_chose()
    all_remorse = remorse_check(coffee)
    if all_remorse:
        order(coffee)







