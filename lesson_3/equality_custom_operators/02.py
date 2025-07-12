class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() == other.name.casefold()
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() != other.name.casefold()
    
garfield = Cat('Garfield')
lasagna = Cat('garfield')

tabby = Cat('Tabby')
print(garfield == lasagna)

print(garfield == tabby)
print(garfield != tabby)

print(garfield == 123)
