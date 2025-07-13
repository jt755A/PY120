# try:
#     number = float(input('Please enter a positive number: '))
#     if number < 0:
#         raise ValueError('Number must be positive!')

# except ValueError:
#     print("That's not a valid number.")

# else:
#     print(f'The result is: {number}')

num = float(input('Please enter a positive number: '))
if num < 0:
    raise ValueError('Negative numbers are not allowed!')
print(f'You entered {num}')