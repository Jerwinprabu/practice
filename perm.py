#!/usr/bin/python

""" Find permutations, combinations, etc """
import random


def permute(n):
    if len(n) == 1:
        yield n
    else:
        for ind, item in enumerate(n):
            for perm in permute(n[:ind] + n[ind+1:]):
                yield [item] + perm
            

def combinations(n, c):
    if c == 0: yield []
    else:
        for i in range(len(n)-c+1):
            for comb in combinations(n[i+1:],c-1):
                yield [n[i]] + comb

def allcomb(n, c):
    pass
    
def test():
    ints = [1, 2, 3, 4]

    print "ints {}".format(ints)
    print "perm: {}".format([x for x in permute(ints)])
    print "perm len: {}".format(len([x for x in permute(ints)]))
    print "comb: {}".format([x for x in combinations(ints, 2)])
    

    
if __name__ == "__main__":
    test()
