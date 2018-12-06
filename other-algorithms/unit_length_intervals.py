# unit_length_intervals.py
print 'hello'
# Let X be a set.  Find the smallest number of unit length unit length intervals
# to cover X
def unit_length_intervals(X):

    # VARIABLES
    list_of_intervals = []

    Y = sorted(X)
    print Y

    start, end = Y[0], Y[0] + 1

    current_interval = (start, end)
    list_of_intervals.append(current_interval)

    for y in Y:
        if y > end:
            start = y
            end = y + 1
            current_interval = (start, end)
            list_of_intervals.append(current_interval)

    return list_of_intervals


X = {0, 0.1, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0, 2.1, 2.7, 5.7, 5.8, 9}
print 'We are doing something'
print unit_length_intervals(X)
