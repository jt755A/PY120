try:
    number1 = float(input('Please enter a number: '))
    number2 = float(input('Please enter a second number: '))
    result = number1 / number2

except (ZeroDivisionError):
    print("Can't divide by zero!")    
except ValueError:
    print("That's not a valid number")

else:
    print(f'The result is {result}')

finally:
    print('End of the program')
