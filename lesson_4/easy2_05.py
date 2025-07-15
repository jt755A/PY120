class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(self):
        greeting = Greeting()
        greeting.greet('Hi')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')


hello = Hello()
hello.hi() # prints 'Hello'

# hello = Hello()
# hello.bye() # AttributeError? No bye method defined for Hello class.

# hello = Hello()
# hello.greet() # Error: greet method requires an argument
# # TypeError

# hello = Hello()
# hello.greet('Goodbye') # Prints 'Goodbye'

Hello.hi() # less readable: 'Hello'?
# actually a TypeError. No `self` is invoked. You are using `hi` method on
# `Hello` class. Invoking instance methods as class methods no instance is 
# passed as self....

