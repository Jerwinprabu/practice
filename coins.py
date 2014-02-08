#!/usr/bin/python

""" Given an infinite number of coins. Find the number of ways of
    representing n cents in cents, nickels, dimes, and quarters """

import random

def ways_internal(cents, den):

    #print "cents {} den {}".format(cents, den)
    if cents == 0:
        return 1
    
    if den == 25:
        count = 0
        max_qtrs = cents / 25
        for i in range(max_qtrs+1):
            count += ways_internal(cents - 25 * i, 10)
    elif den == 10:
        count = 0
        max_dimes = cents / 10
        for i in range(max_dimes+1):
            count += ways_internal(cents - 10 * i, 5)
    elif den == 5:
        count = 0
        max_nick = cents / 5
        for i in range(max_nick+1):
            count += ways_internal(cents - 5 * i, 1)
    else:
        return 1

    return count

def ways(cents):
    return ways_internal(cents, 25)
    
        
    
def test():
    cents = [1, 10, 45, 75, 100]

    for val in cents:
        print "--------------------"
        print "cents: {} ways: {}".format(val, ways(val))
        

    
if __name__ == "__main__":
    test()
