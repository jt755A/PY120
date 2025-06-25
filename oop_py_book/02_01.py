'''

1. Create a Car class that meets these requirements:

Each Car object should have a model, model year, and color provided 
at instantiation time.
You should have an instance variable that keeps track of the current 
speed. Initialize it to 0 when you instantiate a new car.
Create instance methods that let you turn the engine on, accelerate, 
brake, and turn the engine off. Each method should display an 
appropriate message.
Create a method that prints a message about the car's current speed.
Write some code to test the methods.
'''

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.model_year = year
        self.color = color

        self.speed = 0
        self.engine = 'Off'
    
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

rustbucket.get_current_speed()
rustbucket.engine_on()

rustbucket.accelerate(50)
rustbucket.brake(30)
rustbucket.engine_off()
# rustbucket.accelerate(50)




