class Dog:
    def __init__(self, breed):
        self.breed = breed

golden_retriever = Dog('Golden Retriever')
poodle = Dog('Poodle')

print(golden_retriever.breed)
print(poodle.breed)