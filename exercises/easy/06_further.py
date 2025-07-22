class Pet:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def __str__(self):
        return f'a {self.animal} called {self.name}'

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def number_of_pets(self):
        return len(self.pets)

    def print_pets(self):
        for pet in self.pets:
            print(pet)



    # def number_of_pets():
    #     return self.pets



class Shelter:
    def __init__(self):
        self.adoptions = {}
        self.rescued_pets = []
        self.name = 'Midnight Medley'

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        self.adoptions[owner.name] = owner
        if pet in self.rescued_pets:
            self.rescued_pets.remove(pet)


    def print_adoptions(self):
        for name, owner in self.adoptions.items():
            print(f'{name} has adopted the following pets:')
            owner.print_pets()

    def rescue(self, pet):
        self.rescued_pets.append(pet)

    def print_rescues(self):
        print(f'{self.name} has the following unadopted pets:')
        for pet in self.rescued_pets:
            print(pet)

    def number_of_rescues(self):
        return len(self.rescued_pets)


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
bluebell = Pet('parakeet', 'bluebell')

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

shelter.rescue(asta)
shelter.rescue(laddie)
shelter.rescue(fluffy)
shelter.rescue(kat)
shelter.rescue(ben)
shelter.rescue(chatterbox)
shelter.rescue(bluebell)

shelter.print_rescues()

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

print(f"{shelter.name} has {shelter.number_of_rescues()} unadopted pets")

'''
The Animal Shelter has the following unadopted pets:
a dog named Asta
a dog named Laddie
a cat named Fluffy
a cat named Kat
a cat named Ben
a parakeet named Chatterbox
a parakeet named Bluebell
   ...

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
The Animal shelter has 7 unadopted pets.
'''