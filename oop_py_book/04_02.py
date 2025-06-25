'''
2. Write the code needed to make the following code work as shown:
'''
class Vehicle:
    
    counter = 0
    
    def __init__(self):
        Vehicle.counter += 1

    def vehicles():
        return Vehicle.counter


class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass

class Truck(Vehicle):
    pass

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8