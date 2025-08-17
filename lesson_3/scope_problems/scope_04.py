class Dog:
    def __init__(self, breed):
        self._breed = breed

    @property
    def breed(self):
        return self._breed

    # @breed.setter
    # def breed(self, breed):
    #     self._breed = breed

tiger = Dog('Golden Retriever')
fido = Dog('Pug')

tiger._breed = 'labradoodle'
# tiger.breed = 'Labradoodle'
print(tiger.breed)