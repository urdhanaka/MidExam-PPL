import aspectlib


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

    def is_resource_sufficient(self, order):
        can_make = True

        for item in self.resources:
            if order.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False

        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f"Here is your {order.name}. Enjoy!")
        return True


@aspectlib.Aspect(bind=True)
def resource_logging_aspect(cutpoint, *args):
    print("--------------------")
    print("Resource: Starting resource logging...")
    print(f"Resource: Current resources status: {args[0].resources}")
    print(f"Resource: Running method: {cutpoint.__name__}")
    print("--------------------\n")
    print("Result: ")

    yield

    print("\n--------------------")
    print(f"Resource: Final resources status: {args[0].resources}")
    print("--------------------\n")


aspectlib.weave(CoffeeMaker.add_resources, resource_logging_aspect, lazy=True)
aspectlib.weave(CoffeeMaker.make_coffee, resource_logging_aspect, lazy=True)
aspectlib.weave(CoffeeMaker.is_resource_sufficient, resource_logging_aspect, lazy=True)
