class Car:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    manufacturer = 'Nissan'

    def show_manufacturer(self):
        print(f'Instance: {self.manufacturer}, '
              f'class: {self.__class__.manufacturer}')


my_car = Car('Toyota')
my_car.show_manufacturer()