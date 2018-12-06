
# quicksort.py
# K. Sweebe

# The quicksort algorithm takes the right most element of a list as a pivot.
# The next rightmost element (right-1) and the leftmost element are then stored.
def swap(some_list, indexA, indexB):
    tempA = some_list[indexA]
    some_list[indexA] = some_list[indexB]
    some_list[indexB] = tempA
    return some_list

def quicksort(some_list, left_index, pivot_index):
    pivot_index = len(some_list) - 1
    left_index = 0
    right_index = len(some_list) - 2

    if(left >= right)
        print "done"


    print pivot

some_list = [ 1, 5, 3, 7]
quicksort(some_list)

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)TT
