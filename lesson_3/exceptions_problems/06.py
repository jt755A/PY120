my_num_lst = [1, 2, 3, 4, 5, 0]

def invert_numbers(num_lst):
    result = []
    for num in num_lst:
        try:
            result.append(1/num)
        except ZeroDivisionError:
            result.append(float('inf'))

    return result

print(invert_numbers(my_num_lst))