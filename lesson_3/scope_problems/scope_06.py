class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

pupil1 = Student('Bobby')
pupil2 = Student('Bob')

print(f' {pupil1.name}, {pupil1.__class__.school_name}')
print(f' {pupil2.name}, {pupil2.__class__.school_name}')
