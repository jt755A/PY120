
class VehicleMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicle(VehicleMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

    # def range(self):
    #     return self.fuel_capacity * self.fuel_efficiency

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)


class Catamaran(VehicleMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity
        # ... code omitted ...


auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 50, 50.0)

print(auto.fuel_efficiency)
print(auto.fuel_capacity)
print(auto.range())

print(motorcycle.fuel_efficiency)
print(motorcycle.fuel_capacity)
print(motorcycle.range())


print(catamaran.fuel_efficiency)
print(catamaran.fuel_capacity)
print(catamaran.range())

    
