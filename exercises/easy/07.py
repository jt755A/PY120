class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_wheels(self):
        return 4

class Motorcycle:
    def __init__(self, make, model):
        super().__init__(make, model)

    def get_wheels(self):
        return 2

class Truck:
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        return 6