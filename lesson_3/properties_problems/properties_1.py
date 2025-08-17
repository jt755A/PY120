class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

henry = Person('henry')
print(henry.name)

henry.name = 'Harald'
print(henry.name)