"""
subarraySum.py

Given an unsorted array A of size N of non-negative integers, find a continuous
subarray which adds to a given number.

Input:
Takes in an array of integers and a target value to be summed to.

Output:
Returns the indices of the subarray that sums to the target value.
"""


def subarraySum(arr, target):
    # iterate through the elements in the array
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            print sum
            if sum == target:
                return (i,j)
            elif sum > target:
                break


indices = subarraySum([0,1,2,4,8,3], 5)
print "Index of subarray: ", indices
