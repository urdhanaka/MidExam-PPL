import aspectlib

import aspect


class CoffeeMaker:
    def __init__(self, **kwargs: int):
        self.resources = {
            "water": kwargs.get("water", 300),
            "milk": kwargs.get("milk", 200),
            "coffee": kwargs.get("coffee", 100),
        }

    def add_resources(self, resource: str, amount: int):
        if resource not in self.resources:
            print(f"Resource {resource} not found")
            return

        self.resources[resource] += amount

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True

        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False

        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            if self.resources[item] < order.ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                return

            self.resources[item] -= order.ingredients[item]

        print(f"Here is your {order.name}. Enjoy!")


aspectlib.weave(CoffeeMaker.add_resources, aspect.resource_logging_aspect, lazy=True)
aspectlib.weave(CoffeeMaker.make_coffee, aspect.resource_logging_aspect, lazy=True)
aspectlib.weave(
    CoffeeMaker.is_resource_sufficient, aspect.resource_logging_aspect, lazy=True
)
