MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "profit": 0
}

#TODO 1: Ask user what they would like. If report, then Print report (water, coffee, milk remaining and money)

start_coffee_machine=True
while start_coffee_machine:

    request=input("What would you like? (espresso / latte / cappuccino) or report: ").lower()

    def check_water(request):
        req_water= MENU[request]['ingredients']['water']
        return req_water

    def check_coffee(request):
        req_coffee= MENU[request]['ingredients']['coffee']
        return req_coffee

    def check_milk(request):
        req_milk= MENU[request]['ingredients']['milk']
        return req_milk

    def enough_resources(water, coffee, milk):
        return resources["water"] >= water and resources["coffee"] >= coffee and resources["milk"] >= milk

    def transaction(no_of_quarters, no_of_dimes, no_of_nickels, no_of_pennies):
        user_money= (no_of_quarters*0.25) + (no_of_dimes*0.1) + (no_of_nickels*0.05) + (no_of_pennies*0.01)
        if user_money>=MENU[request]['cost']:
            change=round(user_money - MENU[request]["cost"], 2)
            resources["profit"] += MENU[request]['cost']
            print(f"Here is ${change} in change. \nEnjoy your {request}! ☕")
        else:
            print("Sorry, you do not have enough money for this order. Money refunded.")

    def make_coffee(request):
        for ingredient in ["water", "coffee", "milk"]:
            rem_resources = resources[ingredient] - MENU[request]["ingredients"][ingredient]
            resources[ingredient]=rem_resources

    if request=="report":
        print(f"Water: {resources['water']}ml\nCoffee: {resources['coffee']}g\nMilk: {resources['milk']}ml\nMoney: ${resources['profit']}")

    elif request== "off":
        start_coffee_machine=False

    #TODO 2: Check if resources are sufficient depending on the request
    else:
        if enough_resources(check_water(request), check_coffee(request), check_milk(request)):
            quarters=int(input("Please insert coins.\nHow many quarters: "))
            dimes=int(input("How many dimes: "))
            nickels=int(input("How many nickels: "))
            pennies= int(input("How many pennies: "))

            transaction(quarters, dimes, nickels, pennies)
            make_coffee(request)
        else:
            print("Sorry, there aren't enough resources for your coffee choice.")

#TODO 3: Able to process coins only

#TODO 4: Check transaction/calculate change

#TODO 5: MakeCoffee
