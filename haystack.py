#!/usr/bin/python

import random
import math

def nmatch(needle, haystack):
    for i in range(0, len(haystack)-len(needle)+1):
        print haystack[i]
        found = True
        for ind, char in enumerate(needle):
            if needle[ind] != haystack[i+ind]:
                found = False
        if found:
            return i

def countwords(n):
    word_count = 0
    inWord = False
    for i in range(len(n)):
        if not n[i].isspace() and not inWord:
            word_count += 1
            inWord = True
        elif n[i].isspace() and inWord:
            inWord = False
    return word_count

def test():
    needle = "shore"
    haystack = "She sells sea shells by the sea shore"

    print "n: {}, h: {}, off: {}".format(needle, haystack, nmatch(needle, haystack))

    print "hs: {} count: {}".format(haystack, countwords(haystack))

if __name__ == '__main__':
    test()
