#!/usr/bin/python 

""" Reverse the bits of an integer """

x = 123123

def rev(x):
    t = (x & 0xffff) << 16 | ((x >> 16) & 0xffff)
    t = ((t & 0x00ff00ff) << 8) | ((t & 0xff00ff00) >> 8)
    t = ((t & 0x0f0f0f0f) << 4) | ((t & 0xf0f0f0f0) >> 4)
    t = ((t & 0xcccccccc) >> 2) | ((t & 0x33333333) << 2)
    t = ((t & 0xaaaaaaaa) >> 1) | ((t & 0x55555555) << 1)
    return t

print "%s, %s" % (bin(rev(x)), bin(x))
