class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

golden_retriever = Dog('Golden Retriever')
poodle = Dog('Poodle')

print(golden_retriever.get_breed())
print(poodle.get_breed())