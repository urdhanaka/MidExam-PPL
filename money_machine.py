import aspectlib

import aspect


class MoneyMachine:
    CURRENCY = "$"

    def __init__(self):
        self.money = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.money}")

    def add_money(self, money):
        self.money += money

    def payment(self, cost):
        if self.money >= cost:
            self.money -= cost
        else:
            print("Sorry that's not enough money. Money refunded.")


aspectlib.weave(MoneyMachine.add_money, aspect.transaction_aspect, lazy=True)
aspectlib.weave(MoneyMachine.payment, aspect.transaction_aspect, lazy=True)
