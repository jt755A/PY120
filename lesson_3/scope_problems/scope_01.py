class Dog:
    def __init__(self, breed):
        self.breed = breed

tiger = Dog('Golden Retriever')
fido = Dog('Pug')

print(tiger.breed)
print(fido.breed)