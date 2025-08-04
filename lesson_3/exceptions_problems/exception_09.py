numbers = [1, 2, 3, 4, 5]

def sixth_lbyl(nums):
    return None if len(nums) < 6 else nums[5]

def sixth_afnp(nums):
    try:
        return nums[5]
    except IndexError:
        return None

print(sixth_lbyl(numbers))
print(sixth_afnp(numbers))
