#!/usr/bin/python

""" find all subsets of a set """
import random

def subsets(array):
    if len(array):
        yield [array[0]]
        for subset in subsets(array[1:]):
            yield subset
            yield subset + [array[0]]

def genadj(count):
    return count * "()"

def genrec(count):
    for p in paren(count-1):
        yield "(" + p + ")"

def paren(count, gensymm=True):
    if count == 0:
        return
    else:
        if gensymm:
            yield genadj(count)
        for p in paren(count-1, False):
            yield "()" + p
            yield p + "()"
        for p in paren(count-1):
            yield "(" + p + ")"
    
        
    
def test():
    ints = [1, 2, 3]

    print "ints {}".format(ints)
    print "perm: {}".format([x for x in subsets(ints)])
    print "paren: {}".format([x for x in paren(4)])
    

    
if __name__ == "__main__":
    test()
