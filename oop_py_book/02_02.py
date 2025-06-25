'''

Using decorators, add getter and setter methods to your Car class so you can 
view and change the color of your car. You should also add getter methods 
that let you view but not modify the car's model and year. 
Don't forget to write some tests.
'''

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color

        self.speed = 0
        self.engine = 'Off'
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('New color must be a string!')

        self._color = color
    
    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year
    
    def engine_on(self):
        self.engine = 'On'
        print(f'The engine is now {self.engine}')
    
    def accelerate(self, speed_increase):
        if self.engine == 'Off':
            raise ValueError('The car must be on before you can accelerate!')
        
        if not isinstance(speed_increase, int):
            raise TypeError('Acceleration must be an integer')
        
        if speed_increase < 0:
            raise ValueError('Accleration must be positive')
        
        self.speed += speed_increase
        print(f'You sped up by {speed_increase} mph. Current speed '
              f'is now {self.speed} mph')
    
    def brake(self, speed_decrease):
        if self.engine == 'Off':
            raise ValueError('The car must be on before you can brake!')
        
        if not isinstance(speed_decrease, int):
            raise TypeError('Braking force must be an integer')
        
        if speed_decrease < 0:
            raise ValueError('Braking must be positive')
        
        self.speed -= speed_decrease
        print(f'You braked by {speed_decrease} mph. Current speed is now '
              f'{self.speed} mph')

    def engine_off(self):
        self.engine = 'Off'
        self.speed = 0
        print(f'The engine is now {self.engine}')
    
    def get_current_speed(self):
        print(f'The current speed is {self.speed} mph')


rustbucket = Car('Toyota Corolla', 1990, 'Grey')

print(f"My car's color is {rustbucket.color}")
print(f"My car's year is {rustbucket.year}")
print(f"My car is a {rustbucket.model}")
rustbucket.color = 'Orange'
print(f'My car is now {rustbucket.color}')
rustbucket.year = 5000








