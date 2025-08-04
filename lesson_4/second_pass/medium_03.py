class Animal:
    def speak(self, message):
        print(message)

class Cat(Animal):
    def meow(self):
        self.speak('Meow')

class Dog(Animal):
    def bark(self):
        self.speak('Woof! Woof! Woof!')

cat = Cat()
cat.meow()

dog = Dog()
dog.bark()