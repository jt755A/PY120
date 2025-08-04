class Wallet:
    def __init__(self, money):
        self.amount = money

    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.amount + other.amount)

        return NotImplemented

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True