num = float(input('Please enter a number: '))
if num < 0:
    raise ValueError("Number can't be negative")
print(f'The number is: {num}')