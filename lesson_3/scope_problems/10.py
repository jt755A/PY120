class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)               # What will this output?
# Name error or attribute error? 'species' instance variable is not initialized.
# Either use super('species') or add a line for instance variable.