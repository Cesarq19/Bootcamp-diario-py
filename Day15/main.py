# Imports
from data import *
import random as rd
import os

money = 0

# functions
def actual_resources(water, milk, coffee):
    amount_water = resources["water"] - water
    amount_milk = resources["milk"] - milk
    amount_coffee = resources["coffee"] - coffee

    if (amount_water < 0):
        print("Sorry there is not enough water.")
        return False
    elif (amount_milk < 0):
        print("Sorry there is not enough milk.")
        return False
    elif (amount_coffee < 0):
        print("Sorry there is not enough coffee.")
        return False
    else:
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee

        return True

def report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${money}")

def make_coffee(coffee_kind):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    ingredients = MENU[coffee_kind]["ingredients"].keys()
    water, coffee , milk = 0, 0, 0
    cost = MENU[coffee_kind]["cost"]

    if "water" in ingredients:
        water = MENU[coffee_kind]["ingredients"]["water"]
    if "milk" in ingredients:
        milk = MENU[coffee_kind]["ingredients"]["milk"]
    if "coffee" in ingredients:
        coffee = MENU[coffee_kind]["ingredients"]["coffee"]


    if (total >= cost):
        cashback = total - cost
        if(actual_resources(water, milk, coffee)):
            print(f"Here is ${cashback} dollars in change.")
            print(f"Here is your {coffee_kind}. Enjoy!")



def cafe():
    execute = True

    while execute:
        orden = input(" What would you like? (espresso/latte/cappuccino): ")

        if (orden.lower() == "off"):
            execute = False
        elif (orden.lower() == "espresso"):
            make_coffee("espresso")
        elif (orden.lower() == "latte"):
            make_coffee("latte")
        elif (orden.lower() == "cappuccino"):
            make_coffee("cappuccino")
        elif (orden.lower() == "report"):
            report()
        else:
            print("No command found!!")
# Main code
cafe()

