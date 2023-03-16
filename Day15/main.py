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


def print_report() -> None:
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def print_coffee_prices() -> None:
    print("Coffee prices:")
    for coffee in MENU:
        print(f"{coffee.title()} - ${MENU[coffee]['cost']}")


def can_make_coffee(type_of_coffee: str) -> str:
    ingredients = MENU[type_of_coffee]["ingredients"]
    not_enough = ""

    if ingredients["water"] > resources["water"]:
        not_enough = "water"
    elif ingredients["coffee"] > resources["coffee"]:
        not_enough = "coffee"
    elif type_of_coffee in ["latte", "cappuccino"] and ingredients["milk"] > resources["milk"]:
        not_enough = "milk"

    if not_enough:
        return f"Sorry there is not enough {not_enough}."
    else:
        return "Please insert coins."


def change_resources(type_of_coffee: str):
    ingredients = MENU[type_of_coffee]["ingredients"]
    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    if type_of_coffee in ["latte", "cappuccino"]:
        resources["milk"] -= ingredients["milk"]
    resources["money"] += MENU[type_of_coffee]["cost"]


def count_money(type_of_coffee: str):
    quarters = int(input("how many quarters? ")) * 0.25
    dimes = int(input("how many dimes? ")) * 0.1
    nickles = int(input("how many nickles? ")) * 0.05
    pennies = int(input("how many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies

    if total < MENU[type_of_coffee]["cost"]:
        return "Sorry that's not enough money. Money refunded."
    elif total >= MENU[type_of_coffee]["cost"]:
        change_resources(type_of_coffee)
        if total > MENU[type_of_coffee]["cost"]:
            change = total - MENU[type_of_coffee]["cost"]
            print(f"Here is ${change} in change.")
        return f"Here is your {type_of_coffee} ☕️. Enjoy!"


on = True

while on:
    choice = input(
        " If you want to turn off the machine, press 'off'.\n"
        " If you want to know machine report, press 'report'.\n"
        " If you want a cup of coffee, chose one of espresso/latte/cappuccino: "
    )

    if choice == "off":
        on = False
    elif choice == "report":
        print_report()
    elif choice not in ["espresso", "latte", "cappuccino"]:
        print("I don't know what you want")
        on = False
    else:
        print_coffee_prices()
        res = can_make_coffee(choice)
        print(res)

        if res == "Please insert coins.":
            print(count_money(choice))
