#!/usr/bin/python

from math import *

def mysqrt(val):
    x = float(val)
    for i in range(10):
        x = x - (x*x-val)/(2*x)
    return x
        
        
print "sqrt:", sqrt(5)
print "mysqrt:", mysqrt(5)
