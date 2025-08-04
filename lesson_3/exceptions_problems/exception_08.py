students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        age = students[name]
        return age
    except KeyError:
        return 'Student not found'


print(get_age('Doe'))
print(get_age('Brian'))
