class Wallet:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.amount + other.amount)
        
        return NotImplemented

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True