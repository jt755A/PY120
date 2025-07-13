class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

human = Human()
# print(Mammal.legs)
print(human.legs)