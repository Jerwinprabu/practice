#!/usr/bin/python
""" Given an array A of positive inegers, convert
    it to a sorted array with minimum cost. The valid
    operations are:

    1. decrement with cost = 1
    2. delete an element completely from the array with cost=value
       of the element
"""

import random
import math
def makecombs(n):
    for i in range(len(n)-1, -1, -1):
        
def weirdsort(n):
    for i in range(len(n)-1, -1, -1):
        

def test():
    testvec = [random.randint(0, 100) for x in range(15)]
    print "orig: {} sorted: {}".format(testvec, weirdsort(testvec))
    
    

    

if __name__ == '__main__':
    test()
