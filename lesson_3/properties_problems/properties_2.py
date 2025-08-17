class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string!')

        if name == '':
            raise ValueError('Name cannot be empty!')
        self._name = name

henry = Person('henry')
print(henry.name)

henry.name = ''
print(henry.name)