'''
Shelter
    - build nested dictionaries?
        - Owner:
            - pet type: name, pet type: name ....
'''

class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    @property
    def name(self):
        return self.name
    
    @property
    def species(self):
        return self.species

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = 0
    
    @property
    def name(self):
        return self.name

    
    def number_of_pets(self):
        return self.pets


class Shelter:
    adoptions = {}

    def adopt(self, person, pet):
        Shelter.adoptions[person.name] = pet.name

    def print_adoptions(self):
        for person in Shelter.adoptions:
            print(f'{person} has adopted the following pets:')
            for pet in Shelter.adoptions[person]:
                print(f'a test pet')
    


cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")