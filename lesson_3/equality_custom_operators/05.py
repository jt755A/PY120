class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'
    
    @staticmethod
    def _is_numeric(value):
        if isinstance(value, int):
            return True
        
        return value.isdigit()
    
    def __add__(self, other):
        if not isinstance(other, int):
            if not isinstance(other, str):
                return NotImplemented
            
        both_numeric = (self._is_numeric(self.value) and
                        self._is_numeric(other))
        
        if both_numeric:
            return Silly(int(self.value) + int(other))
        else:
            return Silly(str(self.value) + str(other))

    










        # if ((isinstance(self.value, str) and self.value.isdigit())
        #     or isinstance(self.value, int)
        # and str(other).isdigit()):
            





        # if str(self.value).isdigit() and str(other.value).isdigit():
        #     new_value = ''
            
        #     for idx, digit in enumerate(str(self.value)):
        #         new_digit = int(digit) + int(str(other.value)[idx])
        #         new_value += str(new_digit)
            
        #     print(new_value)



'''
Rules
If both x and y can be expressed as integers
    - use iadd
    - mutate EACH digit in x, added to y
        - convert each digit to an int for addition
    - convert value into int at end, return it

- If not, 
    - concatenate string representations of both


Determine both are integer expressible
    - str of both, str.isdigit returns True
    - combine


    
General structure
    - creating a Silly object.
        - value instance variable will either be an int, or a string
    
    - determine how to add either a string or an int to id.
    - Both mutate the original object? Or return a new Silly object?
'''



print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)