class NegativeNumberError(Exception):
    # print("Number can't be negative")
    pass

num = float(input('Please enter a number: '))
if num < 0:
    raise NegativeNumberError("Number can't be negative")
print(f'The number is: {num}')