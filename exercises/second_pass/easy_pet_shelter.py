class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def info(self):
        return f"a {self.species} named {self.name}"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def number_of_pets(self):
        return len(self.pets)

    def add_pet(self, pet):
        self.pets.append(pet)



class Shelter:
    def __init__(self):
        self.adoptions = []
        self.unadopted = []

    def intake(self, pets):
        for pet in pets:
            self.unadopted.append(pet)

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        # now remove pet from unadopted list
        self.unadopted.remove(pet)
        if owner not in self.adoptions:
            self.adoptions.append(owner)

    def print_adoptions(self):
        for person in self.adoptions:
            print(f"{person.name} has adopted the following pets:")
            for pet in person.pets:
                print(pet.info())

    def print_unadopted(self):
        print(f"The Animal shelter has {len(self.unadopted)} unadopted pets.")

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

asta = Pet('dog', 'Asta')
laddie = Pet('dog', 'Laddie')
fluffy = Pet('cat', 'Fluffy')
kat = Pet('cat', 'Kat')
ben = Pet('cat', 'Ben')
chatterbox = Pet('parakeet', 'Chatterbox')
bluebell = Pet('parakeet', 'Bluebell')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()

shelter.intake([cocoa, cheddar, darwin, kennedy, sweetie, molly, chester,
               asta, laddie, fluffy, kat, ben, chatterbox, bluebell])

print(f"Start: {len(shelter.unadopted)}")


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

print(f"End: {len(shelter.unadopted)}")

shelter.print_unadopted()



# adoptions
'''
owner: [pet
'''