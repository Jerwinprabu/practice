#!/usr/bin/python

""" Find permutations, combinations, etc """
import random

def strstrdumb(haystack, needle):
    for i in range(len(haystack)-len(needle)+1):
        match = True
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                match = False
        if match:
            return i
    return -1


def computetable(needle):
    table = [{} for x in range(len(needle))]

def presenttable(needle):
    table = {}
    for i in range(len(needle)):
        if needle[i] in table:
            table[needle[i]].append(i)
        else:
            table[needle[i]] = [i]
    return table
    
def gentable(needle):
    table = [0 for x in needle]
    table[0] = -1
    table[1] = 0
    offs = 0
    for offn in range(2,len(needle)):
        if needle[offn-1] == needle[offs]:
            offs+=1
            table[offn] = offs
            offn+=1
        elif offs > 0:
            offs = table[offs]
        else:
            table[offn] = 0
            offn+= 1
    print "table {}".format(table)
    return table

def strstr(haystack, needle):
    T = gentable(needle)

    i, j = 0, 0 
    while i < len(haystack):
        match = True
        if needle[j] == haystack[i]:
            j+=1
            i+=1
            if j == len(needle):
                return i-len(needle)
        else:
            i = i - T[j]
            j = max(T[j], 0)
    return -1


def match(s, reg):
    assert len(s) == len(reg)
    for x,r in zip(s,reg):
        if r == '?':
            continue
        elif r != x:
            return False
    return True
    
def regex(s, r):
    print s, r
    if r == "": return True
    if s == "": return False

    if len(r) >= 2 and r[1] == "*":
        return any(match(r[0]*n, s[:n]) and regex(s[n:], r[2:]) for n in range(len(s)))
    else:
        return match(s[0], r[0]) and regex(s[1:], r[1:])

def flatten(x):
    if type(x) != type([]):
        yield x
    else:
        for y in x:
            for z in flatten(y):
                yield z
    
def test():
    haystack = "She sells sea shells on the sea shore"
    needle = "on the"

    print "hay: {} needle: {} off: {}".format(haystack, needle, strstr(haystack, needle))

    haystack = "ababcabcd"
    needle = "abcd"

    print "hay: {} needle: {} off: {}".format(haystack, needle, strstr(haystack, needle))

    for i in range(0,10):
        print i
        i+= 2

    print regex("DEEEEERRRRFF", "DE*R*F")
    for y in flatten([[1], [2,3]]):
        print y
    #flatten([[1], 2, [[3, 4], 5], 6, [], [7, [8, [9, 10, 11]]]])
        


    
if __name__ == "__main__":
    test()
