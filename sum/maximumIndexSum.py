"""
maximumIndexSum.py

Given an array of integers, find the maximum of j - i subjected to the
constraint A[i] <= A[j]

Input:
An array of integers

Output:
A tuple consisting of the max distance seen and the corresponding indices
"""

def maximumIndexSum(arr):
    max_distance = -1
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] <= arr[j]:
                if j - i > max_distance:
                    max_distance = j - i
                    max_tuple = (i, j)
    return (max_distance, max_tuple)

arr = [3, 5, 4, 2]
ans = maximumIndexSum(arr)
print ans
