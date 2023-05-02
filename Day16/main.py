# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# table.align = "l"

# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

process = True

while process:
    kind_coffee = input("What would you like? ("+ menu.get_items() +"):").lower()
    
    if kind_coffee == "off":
        process = False
    elif kind_coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(kind_coffee)
        if coffee != None:
            if coffee_maker.is_resource_sufficient(coffee):
                coffee_maker.make_coffee(coffee)
                
                print("Please insert coins.")
                quarters = int(input("how many quarters?: "))
                dimes = int(input("how many dimes?: "))
                nickles = int(input("how many nickles?: "))
                pennies = int(input("how many pennies?: "))

                total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                
                money_machine.make_payment(total)

                
            