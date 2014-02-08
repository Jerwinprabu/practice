#!/usr/bin/python
""" Find top log(n) or top sqrt(n) values in an array of integers
in less than linear time. """

""" complexity O(n) """

import random
import math

def partition(n):
    """ parition array at random pivot point, return the offset of pivot"""
    offset = random.randint(0,len(n)-1)
    n[0], n[offset] = n[offset], n[0]

    left, right = 1, len(n)-1
    pivot = n[0]
    while left <= right:
        if n[right] >= pivot:
            right -= 1
        else:
            n[right], n[left] = n[left], n[right]
            left += 1
    n[0], n[left-1] = n[left-1], n[0]
    return left-1
    
def topNInternal(n, count):
    """ Don't call this one directly""" 
    if count == len(n): return n[:]
    assert len(n) != 0
    assert count != 0
    mid = partition(n)
    len_a = mid
    len_b = len(n)-mid-1
    print "len_a {} len_b {}, count {}\n".format(len_a, len_b, count)
    if len_b > count:
        return topNInternal(n[mid+1:], count)
    elif len_b == count:
        return n[mid+1:]
    elif len_b+1 == count:
        return n[mid:]
    else:
        return n[mid:] + topNInternal(n[:mid], count-len_b-1)

def topN(n):
    """ return the top log(n) values in the array """ 
    count = math.floor(math.log(len(n), 2))
    return topNInternal(n, count)    

def test():
    for i in range(10, 15):
        array = [random.randint(0, 1000) for i in range(0, i)]
        print "{} topN:{}\nsorted: {}".format( array, topN(array), sorted(array))

if __name__ == '__main__':
    test()
