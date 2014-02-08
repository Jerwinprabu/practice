#!/usr/bin/python
import random

""" Sorted array with non-distinct elements, find the element i, where i=A[i] """

def findelem(array, start, end):
    mid = (start + end) / 2

    if mid == array[mid]:
        return mid
    else:
        if start == end:
            return -1
        elif array[mid] > mid:
            ret = findelem(array, array[mid], end)
            if ret != -1:
                return ret
            return findelem(array, start, mid-1)
        elif array[mid] < mid:
            ret = findelem(array, start, array[mid])
            if ret != -1:
                return ret
            return findelem(array, mid+1, end)

def test():
    inp = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    print "arr: {} off: {}".format(inp, findelem(inp, 0, len(inp)-1))
    
if __name__ == '__main__':
    test()
