class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

print(Cat.cats_count())
cat1 = Cat('tabby')
cat2 = Cat('black')
print(Cat.cats_count())
