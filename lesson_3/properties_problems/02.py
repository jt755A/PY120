class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Name must be a string')
        
        elif not new_name:
            raise ValueError('Name cannot be empty')
        self._name = new_name

chuck = Person('Chuck')
print(chuck.name)

chuck.name = 'Charlie'
print(chuck.name)

chuck.name = ''
print(chuck.name)
# print(f'{chuck.name=}')


# chuck.name = ('Charles',)