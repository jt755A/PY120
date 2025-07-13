class Student:
    school_name = 'Oxford'

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    def __init__(self, name):
        self.name = name

print(Student.get_school_name())
print(Student.school_name)

# student1 = Student('Ron')
# student2 = Student('Griselda')

# print(student1.name, student1.__class__.school_name)
# print(student2.name, student1.__class__.school_name)


# print(student1.school_name)
# print(student1.__class__.school_name)
# print(Student.school_name)
