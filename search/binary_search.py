def binary_search_helper(A, x, min, max):
    print "\n\n", min, max
    if ( min <= max):
        mid = (min + max)/2
        print "mid: {}".format(mid)
        print "A[mid]: {}".format(A[mid])
        print "x: {}".format(x)
        if (x == A[mid]):
            print "here"
            return True
        elif (x < A[mid]):
            return binary_search_helper(A, x, min, mid)
        else:
            return binary_search_helper(A, x, mid, max)
    return False

def binary_search(A, x):
    return binary_search_helper(A, x, 0, len(A) - 1)


def search_check():
    A = [1, 2, 3, 4, 5]
    x = 0
    y = 1
    z = 3
    p = 5
    q = 6

    print "The array: {}".format(A)
#    print "    - element x = {0}     result = {1}".format(x, binary_search(A,x))
    print "    - element y = {0}     result = {1}".format(y, binary_search(A,y))
    print "    - element b = {0}     result = {1}".format(2, binary_search(A,2))
    print "    - element z = {0}     result = {1}".format(z, binary_search(A,z))
#    print "    - element p = {0}     result = {1}".format(p, binary_search(A,p))
#    print "    - element q = {0}     result = {1}".format(q, binary_search(A,q))

search_check()  
