"""
 maximum_subsequence.py

 Given an array of integers (positive and negative), find the
 indices left and right such that the sum
 A[left] + A[left+1] + ... A[right-1] + A[right] is maximized
"""

# some code to generate the sample array for testing and to create the specified
# size so the three below algorithms can be tested with different input sizes

from matplotlib import pyplot
import numpy as np
import timeit
from functools import partial
import random

# Sample array for testing. Feel free to add additional small examples
sample_A = [-2, -5, 6, -2, -3, 1, 5, -6]

# Random input of 100 elts for additional testing
random_A = random.sample(range(-100,100), 100)


"""
The following seqsum is 1 of three ways presented in this script to get a
maximum subarray sum.

"""
def max_seqsum_part_a(A, left, right):
    """returns max sum of contiguous subarray within A[left...right]"""
    if right == left:
        return A[left]

    # set mid to the floor of left+right /2
    mid = (left + right) / 2
    left_max_sum = max_seqsum_part_a(A, left, mid)
    right_max_sum = max_seqsum_part_a(A, mid + 1, right)

    # find max sequence sum crossing left and right halves
    cross_max_sum = 0
    i = left
    while i <= mid:
        temp_sum = A[i]
        j = i + 1
        while j <= right:
            temp_sum = temp_sum + A[j]
            cross_max_sum = max(cross_max_sum, temp_sum)
            j = j + 1
        i = i + 1

    # returns the largest of those three sums
    return max(left_max_sum, right_max_sum, cross_max_sum)

maximum = max_seqsum_part_a(sample_A, 0, len(sample_A)-1)
print 'The max subarray sum for test array is', maximum
