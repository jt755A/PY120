class MovingMixin:
    def walk(self):
        return f"{self.appelation()} {self.gait()} forward"

    def appelation(self):
        if self.__class__ == Noble:
            return f"{self.title} {self.name}"
        else:
            return f"{self.name}"

class Person(MovingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(MovingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(MovingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

class Noble(MovingMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def gait(self):
        return 'struts'

    # def walk(self):
    #     return self.title + f" {super().walk()}"


byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"