class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return self.wheels

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.wheels = 4

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.wheels = 2

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload
        self.wheels = 6

car = Car('Toyota', 'Corolla')
print(car.info())
print(car.get_wheels())


motorcycle = Motorcycle('Yamaha', 'bike')
print(motorcycle.info())
print(motorcycle.get_wheels())


truck = Truck('Ford', 'FE150', 5000)
print(truck.info())
print(truck.get_wheels())

