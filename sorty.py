#!/usr/bin/python

""" Find the smallest subsequence within an array that needs to
    be sorted to sort the entire array """
def findLeftSeq(seq):
    prev = seq[0]
    for i in range(1,len(seq)):
        if seq[i] >= prev:
            prev = seq[i]
        else:
            return i-1
        
def findRightSeq(seq):
    prev = seq[-1]
    for i in range(len(seq)-2, -1, -1):
        if seq[i] <= prev:
            prev = seq[i]
        else:
            return i+1

def findInd(seq):
    leftInd = findLeftSeq(seq)
    rightInd = findRightSeq(seq)

    # If the sequence is already sorted
    if leftInd == len(seq)-1:
        return 0, len(seq)-1

    # Find the min of middle and right, and max of left
    minRightMid = min(seq[leftInd+1:])
    maxLeft = max(seq[:leftInd+1])

    # shrink the left partition
    while maxLeft > minRightMid:
        minRightMid = min(minRightMid, seq[leftInd])
        leftInd-=1
        maxLeft = seq[leftInd]

    # find the max of the middle and left, and min of the right
    minRight = min(seq[rightInd:])
    maxLeftMid = max(seq[:rightInd])

    # shrink the right partition
    while minRight < maxLeftMid:
        maxLeftMid = max(maxLeftMid, minRight)
        rightInd += 1
        minRight = seq[rightInd]
    
    #print "l: {}, r: {}".format(seq[0:leftInd+1], seq[rightInd:])

    return leftInd+1, rightInd-1
    

def test():
    seq = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

    x, y = findInd(seq)

    print "seq: {}, ({},{})".format(seq, x, y)
    

if __name__ == '__main__':
    test()
