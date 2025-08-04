class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    @staticmethod
    def is_num(value):
        if isinstance(value, int):
            return True
        # elif isinstance(value, str):
        return value.isdigit()

    def __add__(self, other):
        if (not isinstance(other, int) and not isinstance(other, str)):
            return NotImplemented
        # both expressible as ints
        if Silly.is_num(self.value) and Silly.is_num(other):
            return Silly(int(self.value) + int(other))

        # in any other case (at least one is not numeric)
        else:
            return Silly(str(self.value) + str(other))



# print(Silly.is_num('abc'))
# print(Silly.is_num(123))
# print(Silly.is_num('123'))



print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)

'''
If both x and y can be expressed as integers, compute the sum of the integer values of x and y.
Otherwise, concatenate the string values of x and y.
'''