"""
twoSum takes in an array of integers and a single integer target.
The goal is to find two elements i,j such that i + j = target.
We can assume there will only be one solution
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0, len(nums)-1):

        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

print twoSum([1, 2, 3, 4], 6)


"""
twoSumHash takes in an array of integers and a single integer target.
The goal is to find two elements i,j such that i + j = target.
We can assume there will only be one solution

twoSumHash is faster than twoSum because it implements a hash table that
allows for constant time lookup
"""

def twoSumHash(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_lookup = set()
    for i in range(0, len(nums)-1):
        num_lookup.add(nums[i])
        if (target - nums[i]) in num_lookup:
            return [nums[i], target-nums[i]]
    return "i, j DNE st i + j = target"


print twoSumHash([7, 3, 9, 4, 1], 13)
