#!/usr/bin/python

""" Find the least common multiple of an array """
import random

def lcm(n):
    n_sorted = sorted(n)
    found = False
    while not found:
        for x in range(1, len(n_sorted)):
            n_sorted[x] = n_sorted[x] % n_sorted[0]
        n_sorted = [x for x in n_sorted if x != 0]
        print n_sorted
        if len(n_sorted) == 1: break
        n_sorted = sorted(n_sorted)
    mult = 1
    print n_sorted[0]
    for x in n: mult *= x
    while mult
    return mult / n_sorted[0]
    
            

def test():
    array = [random.randint(4, 60) for x in range(3)]

    print "arr: {} lcm: {}".format(array, lcm(array))

if __name__ == "__main__":
    test()
