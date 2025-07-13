class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

student1 = Student('Ron')
student2 = Student('Griselda')

print(student1.name, student1.__class__.school_name)
print(student2.name, student1.__class__.school_name)


# print(student1.school_name)
# print(student1.__class__.school_name)
# print(Student.school_name)
