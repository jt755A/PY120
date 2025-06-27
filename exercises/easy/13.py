class Transform:
    def __init__(self, text):
        self.text = text

    def uppercase(self):
        return self.text.upper()    
    
    @classmethod
    def lowercase(cls, strng):
        return strng.lower()

    


my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz