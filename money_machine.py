import aspectlib


class MoneyMachine:
    def __init__(self):
        self.money = 0

    def report(self):
        print(f"Money: ${self.money}")

    def add_money(self, money):
        self.money += money


@aspectlib.Aspect(bind=True)
def transaction_aspect(cutpoint, *args):
    print("--------------------")
    print("Transaction: Starting transaction...")
    print(f"Transaction: Current money status: {args[0].money}")
    print(f"Transaction: Running method: {cutpoint.__name__}")

    yield

    print(f"Transaction: Final money: {args[0].money}")
    print("--------------------\n")


aspectlib.weave(MoneyMachine.add_money, transaction_aspect, lazy=True)
