class MenuItem:
    def __init__(self, name: str, water: int, milk: int, coffee: int, cost: float):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        options = ""

        for item in self.menu:
            options += f"{item.name}\n"

        return options

    def find_drink(self, order_name: str):
        return_value = MenuItem("", 0, 0, 0, 0.0)

        for item in self.menu:
            if item.name == order_name:
                return_value = item

        return return_value
