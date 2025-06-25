'''
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. 
The class should have at least one instance variable that gets 
initialized by the initializer.

What class you create doesn't matter, provided it satisfies the 
above requirements.

Create a class using the class statement. Within which, we call the initializer method.
Assigning a name that will be initialized for any instance of the class.

Create an object by calling the class as a function, with the object 
name as an argument. This is assigned to a variable.

'''

class Book:

    def __init__(self, name):
        self.name = name

don_quixote = Book('Don Quixote')

