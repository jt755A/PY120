class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    pass

bird1 = Sparrow('sparrow')
print(bird1.species)