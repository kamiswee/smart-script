# merge_sort first divides the array into equal halves and then combines them in a sorted manner

def merge_sort(list):
    if len(list) <= 1:
        return list

    # else, find the middle and divide
    middle = len(list) / 2
    left_list = list[:middle]
    right_list = list[middle:]
    return merge(left_list, right_list)

def merge(left_list, right_list):
    res = []
    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        else:
            res.append(right_list[0])
            right_list.remove(right_list[0])
    if len(left_list) == 0:
        res = res + right_list
    else:
        res = res + left_list
    return res




list = [4, 28, 2, 15, 12, 27]
list = merge_sort(list)
print list
