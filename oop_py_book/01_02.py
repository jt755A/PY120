'''
Given an instance of a Foo object, show two ways to print 
I am a Foo object without hardcoding the word Foo.

Solution
'''

class Foo:

    pass

#     def __init__(self, name):
#         self.name = name
#         type_name = type(self).__name__
#         # print(f'I am a {type_name} object')
    
#     def speak(self):
#         # print(f'I am a {type(self).__name__} object')
#         print(f'I am a {self.__class__.__name__} object')


foo1 = Foo()

print(f'I am a {type(foo1).__name__} object')
print(f'I am a {foo1.__class__.__name__} object')


# foo1.speak()