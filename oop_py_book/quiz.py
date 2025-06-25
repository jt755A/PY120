# class Cat:
#     pass

# whiskers = Cat()
# ginger = Cat()
# paws = Cat()

# print(id(whiskers))
# print(id(ginger))
# print(id(paws))

# print(id(whiskers))
# print(id(ginger))
# print(id(paws))

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(self.sound())

#     def sound(self):
#         return f'{self.name} says '

# class Cow(Animal):
#     def sound(self):
#         return super().sound() + 'moooooooooooo!'

# daisy = Cow('Daisy')
# daisy.speak()

# class Person:
#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         self._name = name

# kate = Person()
# kate.name = 'Kate'
# print(kate.name)

# class Person:
#     @property
#     def full_name(self):
#         return f'{first_name} {last_name}'
    
#     @property
#     def first_name(self):
#         return self._first_name

#     @first_name.setter
#     def first_name(self, first_name):
#         self._first_name = first_name

#     @property
#     def last_name(self):
#         return self._last_name

#     @last_name.setter
#     def last_name(self, last_name):
#         self._last_name = last_name

# mike = Person()
# mike.first_name = 'Michael'
# mike.last_name = 'Garcia'
# print(mike.full_name)         # Michael Garcia

# class Student:
#     def __init__(self, name):
#         self._name = name
#         self._grade = None

#     @property
#     def grade(self):
#         return self._grade
    
#     def change_grade(self, grade):
#         self._grade = grade

# priya = Student('Priya')
# priya.change_grade('A')
# print(priya.grade)            # A

class Person:
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

kate = Person()
kate._name = 'Kate'
print(kate.get_name())