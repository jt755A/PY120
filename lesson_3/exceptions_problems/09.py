numbers = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 4, 5, 6]


def LBYL_6th_element(lst):
    SIXTH = 6
    if SIXTH > len(lst):
        return None
    else:
        return lst[SIXTH - 1]
    
def AFNP_6th_element(lst):
    SIXTH_IDX = 6
    try:
        return lst[SIXTH_IDX - 1]
    except IndexError:
        return None
    
print(LBYL_6th_element(numbers))
print(AFNP_6th_element(numbers))

print(LBYL_6th_element(numbers2))
print(AFNP_6th_element(numbers2))

