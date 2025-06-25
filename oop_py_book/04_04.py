'''
4. Print the method resolution order for cars, trucks, boats, 
and vehicles as defined in the previous exercise.
'''

class SignalMixin:

    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')
    

class Vehicle:
    
    counter = 0
    
    def __init__(self):
        Vehicle.counter += 1

    def vehicles():
        return Vehicle.counter


class Car(SignalMixin, Vehicle):
    
    def __init__(self):
        super().__init__()

class Boat(Vehicle):
    pass

class Truck(SignalMixin, Vehicle):
    
    def __init__(self):
        super().__init__()

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())




# Cars: Car -> SignalMixin -> Vehicle -> Object
# Trucks: Truck -> SignalMixin -> Vehicle -> Object
# Boats: Boat -> Vehicle -> Object
# Vehicles: Vehicle -> Object