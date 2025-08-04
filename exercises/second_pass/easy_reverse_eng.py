class Transform:

    def __init__(self, string):
        self.data = string

    def uppercase(self):
        if isinstance(self.data, str):
            return self.data.upper()

    @classmethod
    def lowercase(cls, text):
        return text.casefold()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz