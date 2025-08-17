class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name == other.name

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name != other.name

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name < other.name

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name > other.name

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name <= other.name

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name >= other.name

feline = Cat('feline')
feline2 = Cat('feline')
scruffy = Cat('scruffy')
lst = []

print(feline == feline2)
print(feline == scruffy)
print(scruffy == lst)

print(feline != feline2)
print(feline != scruffy)
print(scruffy != lst)

print(feline < feline2)
print(feline < scruffy)
print(scruffy < lst)

print(feline > feline2)
print(feline > scruffy)
print(scruffy > lst)

print(feline >= feline2)
print(feline >= scruffy)
print(scruffy >= lst)

print(feline <= feline2)
print(feline <= scruffy)
print(scruffy <= lst)
