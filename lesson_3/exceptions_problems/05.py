# try:
#     number = float(input('Please enter a positive number: '))
#     if number < 0:
#         raise ValueError('Number must be positive!')

# except ValueError:
#     print("That's not a valid number.")

# else:
#     print(f'The result is: {number}')

class NegativeNumberError(Exception):
    def __init__(self, message='Negative numbers are not allowed!'):
        super().__init__(message)        


num = float(input('Please enter a positive number: '))
if num < 0:
    raise NegativeNumberError
print(f'You entered {num}')