'''
5.
if not first_name.isalpha():
            raise ValueError('Name must be alphabetic')
        first_name = first_name.title()
        
        self.last_name = last_name
        if not last_name.isalpha():
            raise ValueError('Name must be alphabetic')
'''

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        if not first_name.isalpha():
            raise ValueError('Name must be alphabetic')
        # self.first_name = first_name.title()

        self.last_name = last_name.title()
        if not last_name.isalpha():
            raise ValueError('Name must be alphabetic')
        # self.last_name = last_name.title()
        
        
    @property
    def name(self):
        
        # return f'{first_name} {last_name}'
    
    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)

    # @classmethod
    # def _validate(cls, name):
    #     if not name.isalpha():
    #         raise ValueError('Name must be alphabetic.')


friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'BlakeJohn')
print(friend.name)
# ValueError: Name must be alphabetic.
