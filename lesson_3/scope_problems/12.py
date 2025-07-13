class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    # sound = "roar"
    pass

print(Lion.make_sound())

# It will print 'roar'.
# the Lion subclass inherits the make_sound class method from its superclass Cat.
# this method uses cls: this means whichever class calls the method will return
# its class_variable `sound`.

# If Lion had no `sound` class variable, the method resolution order would search and
# return the Lion `sound` variable.