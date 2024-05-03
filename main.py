from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

CHOICES = ["off", "report"]

for item in menu.menu:
    CHOICES.append(item.name)

while True:
    choice = input(f"What would you like? ({CHOICES}): ")
    if choice == "off":
        print("Turning off... Goodbye!\n")
        break
    elif choice == "report":
        print("Coffee Machine report:")
        coffee_maker.report()
        print("\nMoney Machine report:")
        money_machine.report()
        print("")
    else:
        if choice not in CHOICES:
            print("Menu is not available on the menu")
        else:
            requested_menu = menu.find_drink(choice)
            if not coffee_maker.is_resource_sufficient(requested_menu):
                print("Resources is not sufficient")
            else:
                coffee_maker.make_coffee(requested_menu)
                money_machine.add_money(requested_menu.cost)
