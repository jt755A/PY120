class GoodDog:

    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def speak(self):
        return f'{self.__name} says arf!'

sparky = GoodDog('Sparky', 5)

sparky.__name = 'Billy'
print(sparky.__name)         # Fido
print(sparky.speak())        # Sparky says arf!

sparky._GoodDog__name = 'Fido'
print(sparky._GoodDog__name) # Fido
print(sparky.speak())        # Fido says arf!
print(sparky.__name)