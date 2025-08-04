class FuelMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

    def set_fuel_efficiency(self, kilometers_per_liter):
        self.fuel_efficiency = kilometers_per_liter

    def set_fuel_capacity(self, liters_of_fuel_capacity):
        self.fuel_capacity = liters_of_fuel_capacity


class WheeledVehicle(FuelMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        # self.set_fuel_efficiency(kilometers_per_liter)
        # self.set_fuel_capacity(liters_of_fuel_capacity)
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


class WaterVehicle(FuelMixin):
    def __init__(self,
                 number_propellers,
                 number_hulls,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        # self.set_fuel_efficiency(kilometers_per_liter)
        # self.set_fuel_capacity(liters_of_fuel_capacity)
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        # return (self.fuel_capacity * self.fuel_efficiency) + 10
        return super().range() + 10

class Motorboat(WaterVehicle):
    def __init__(self,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        super().__init__(1,
                         1,
                         kilometers_per_liter,
                         liters_of_fuel_capacity)


class Catamaran(WaterVehicle):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(number_propellers,
                         number_hulls,
                         kilometers_per_liter,
                         liters_of_fuel_capacity)

auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)
motorboat = Motorboat(500, 100)

print(f'{auto.fuel_efficiency=}')             # 50
print(f'{auto.fuel_capacity=}')               # 25.0
print(f'{auto.range()=}')                     # 1250.0

print(f'{motorcycle.fuel_efficiency=}')       # 80
print(f'{motorcycle.fuel_capacity=}')         # 8.0
print(f'{motorcycle.range()=}')               # 640.0

print(f'{catamaran.fuel_efficiency=}')        # 1.5
print(f'{catamaran.fuel_capacity=}')          # 600
print(f'{catamaran.range()=}')                # 900.0

print(f'{motorboat.fuel_efficiency=}')
print(f'{motorboat.fuel_capacity=}')
print(f'{motorboat.range()=}')