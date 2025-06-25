'''
3. Add a method to the Car class that lets you spray paint the car a 
specific color. Don't use a setter method for this. Instead, create 
a method whose name accurately describes what it does. 
Don't forget to test your code.
'''

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color

        self.speed = 0
        self.engine = 'Off'
    
    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year
    
    def spray(self, new_color):
        self.color = new_color
        print(f"Your car is now {new_color}")
    
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
rustbucket.spray('emerald')

# print(f"My car's color is {rustbucket.color}")
# print(f"My car's year is {rustbucket.year}")
# print(f"My car is a {rustbucket.model}")
# rustbucket.color = 'Orange'
# print(f'My car is now {rustbucket.color}')
# rustbucket.year = 5000








