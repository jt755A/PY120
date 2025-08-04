def inverse_numbers(lst):
    try:
        inverse = [1/num for num in lst]
    except (TypeError, ZeroDivisionError) as e:
        print(e)
    else:
        return inverse

print(inverse_numbers([1, 2, 3, 4, set()]))

