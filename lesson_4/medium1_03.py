class Animal:
    def speak(self, sound):
        print(sound)

class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    def bark(self):
        self.speak('Woof! Woof! Woof!')

cat1 = Cat()
cat1.meow()

dog1 = Dog()
dog1.bark()
