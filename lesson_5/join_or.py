# def join_or(lst, delimiter=', ', end='or'):
#     if len(lst) == 1:
#         return str(lst[0])
    
#     else:
#         # return (delimiter.join(str(element) for element in lst[:-2])
#         #          + end + f' {lst[-1]}')

#         result = ''
#         for idx, element in enumerate(lst):
#             result += str(element)
            
#             if idx == len(lst) - 2:
#                 result += f' {end} '

#             elif idx == len(lst) - 1:
#                 break
            
#             else:   
#                 result += delimiter

#         return result
    
def _join_or(choices, separator=", ", conjunction="or"):
    if len(choices) == 1:
        return str(choices[0])
    if len(choices) == 2:
        return f"{choices[0]} {conjunction} {choices[1]}"

    last = choices[-1]
    initial = choices[:-1]
    initial = [str(choice) for choice in initial]
    prompt = separator.join(initial)
    return f"{prompt}{separator}{conjunction} {last}"
    

print(join_or([1]))                # => "1,"
print(join_or([1, 2, 3]))                # => "1, 2, or 3"
print(join_or([1, 2]))                   # => "1 or 2"
print(join_or([1, 2, 3], '; '))          # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))   # => "1, 2, and 3"