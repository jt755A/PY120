try:
    number1 = float(input('Please enter a number: '))
    number2 = float(input('Please enter a second number: '))
    result = number1 / number2

except (ZeroDivisionError, ValueError) as e:
    print(e.__class__.__name__)

else:
    print(f'The result is {result}')

finally:
    print('End of the program')
