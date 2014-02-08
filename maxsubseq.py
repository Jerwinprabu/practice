#!/usr/bin/python

""" Find the maximum subsequence in an array of integers """

def maxsubseq(seq):
    max_sum, max_start, max_end = -1000, 0, 0
    cur_sum, cur_start, cur_end = 0, 0, 0

    for i, elem in enumerate(seq):
        if cur_sum + elem > elem:
            cur_sum += elem
            cur_end = i
        else:
            cur_sum = elem
            cur_start, cur_end = i, i
        if cur_sum > max_sum:
            max_sum, max_start, max_end = cur_sum, cur_start, cur_end
    return max_start, max_end
            
def test():
    seq = [2, 3, -8, -1, 2, 4, -2, 3]


    print "seq: {}, {}".format(seq, maxsubseq(seq))
    

if __name__ == '__main__':
    test()
