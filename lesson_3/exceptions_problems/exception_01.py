# try :
#     number1 = input('Please enter the first number: ')
#     int(number1)
# except ValueError:
#     print("That's not a valid number!")

# try :
#     number2 = input('Please enter the second number: ')
#     int(number2)
# except ValueError:
#     print("That's not a valid number!")

number1 = input('Please enter the first number: ')
number2 = input('Please enter the second number: ')

try:
    result = int(number1) / int(number2)
    print(result)

except ValueError:
    print("That's not a valid number!")

except ZeroDivisionError:
    print("Infinity / cannot calculate: dividing by zero")