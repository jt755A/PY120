class Cat:
    @classmethod
    def generic_greeting(self):
        print("Hello! I'm a cat!")

Cat.generic_greeting()

kitty = Cat()
type(kitty).generic_greeting()