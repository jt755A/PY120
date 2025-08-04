try:
    num1 = float(input('Please enter the first number: '))
    num2 = float(input('Please enter the second number: '))
    result = num1 / num2
except ValueError:
    print('Please enter valid numbers!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
else:
    print(f'Result is: {result}')
finally:
    print('End of the program')

