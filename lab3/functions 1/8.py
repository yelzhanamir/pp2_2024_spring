def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False


input = input("enter array ")
nums = [int(x) for x in input.split()]
print(has_33(nums))