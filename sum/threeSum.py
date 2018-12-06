"""
threeSum takes in two parameters, an array of
integers nums and a single integer targetself.

The goal is to return a set of three-tuples such that
the values of the three-tuples equals the target
"""
from itertools import combinations
def threeSum(nums, target):
    answers = []
    three_elt_sets = list(combinations(nums, 3))
    for set in three_elt_sets:
        if set[0] + set[1] + set[2] == target:
            answers.append(set)
    return set(answers)

print threeSum([1,0,-1,2,0,4,0], 0)
