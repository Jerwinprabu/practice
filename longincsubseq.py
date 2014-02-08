#!/usr/bin/python
from collections import deque

""" Find the longest increasing subsequence in an array of integers """

def longest_inc_subseq(seq):
    lengths = [0] * len(seq)
    prev = [0] * len(seq)   

    for i, item in enumerate(seq):
        found = False
        longest_length = -1
        prev_elm = -1
    
        for j, end in enumerate(seq[:i]):
            if (end < item) and (lengths[j] + 1 > longest_length):
                longest_length = lengths[j] + 1 
                prev_elm = j
                found = True
        if not found:
            prev[i] = -1
            lengths[i] = 1
        else:
            prev[i] = prev_elm
            lengths[i] = longest_length
    
    ret = deque()
    index, size = max(enumerate(lengths), key = lambda a: a[1])
    while index != -1:
        ret.appendleft(seq[index])
        index = prev[index]
    return list(ret)

if __name__ == "__main__":
    seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print "{} {}".format(seq, longest_inc_subseq(seq))

"""
def subseq(seq):
    len_seq = [0 for i in seq]
    pre_seq = [-1 for i in seq]

    for i,element in enumerate(seq):
        max_len = 1
        for j in range(i):
            if seq[i] >= seq[j] and len_seq[j]+1 > max_len:
                max_len = len_seq[j] + 1
                pre_seq[i] = j
        len_seq[i] = max_len

    max_sub_end = 0
    max_sub_len = 0
    for i in range(len(seq)):
        if len_seq[i] > max_sub_len:
            max_sub_len = len_seq[i]
            max_sub_end = i

    sub_seq = []
    i = max_sub_end
    while i != -1:
        sub_seq = [seq[i]] + sub_seq
        i = pre_seq[i]

    return sub_seq   
    
def test():
    seq = [1, 4, 3, 2, 6, 7, 5, 6, 6.5]
    print "seq: {}, {}".format(seq, subseq(seq))
    

if __name__ == '__main__':
    test()
"""
