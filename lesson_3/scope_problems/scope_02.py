class Dog:
    def __init__(self, breed):
        self._breed = breed

    @property
    def breed(self):
        return self._breed

tiger = Dog('Golden Retriever')
fido = Dog('Pug')

print(tiger.breed)
print(fido.breed)