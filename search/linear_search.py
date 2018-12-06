"""
linear_search.py

Takes in an array and a target and returns the index of the target or -1 if not found
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print linear_search([11,2,3,4], 4)

print linear_search([11,2,3,4], 1)
