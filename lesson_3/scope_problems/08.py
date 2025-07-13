class Car:
    manufacturer = 'Honda'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(f'{self.__class__.manufacturer=}')
        print(f'{self.manufacturer=}')

car1 = Car('Ford')

car1.show_manufacturer()