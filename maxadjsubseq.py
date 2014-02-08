#!/usr/bin/python


def adjsubseq(seq, off, cache):
    if off in cache:
        return cache[off]
    sum_a, sum_b = 0, 0
    if off+2 < len(seq):
        sum_a, seq_a = adjsubseq(seq, off+2, cache)
        sum_a += seq[off]
        seq_a = [seq[off]] + seq_a
    if off+3 < len(seq):
        sum_b, seq_b = adjsubseq(seq,off+3, cache)
        sum_b += seq[off]
        seq_b = [seq[off]] + seq_b
    if sum_a or sum_b:
        if sum_a > sum_b:
            ans = (sum_a,seq_a)
        else:
            ans = (sum_b,seq_b)
    else:
        ans = (seq[off],[seq[off]])
    cache[off] = ans
    return ans
        
        

def maxsubseq(seq):
    cache = {}
    sum_a, seq_a = adjsubseq(seq, 0, cache)
    sum_b, seq_b = adjsubseq(seq, 1, cache)

    if sum_a > sum_b: return (sum_a, seq_a)
    else: return (sum_b, seq_b)

def test():
    test = [1,4,3,4,5,6,7]
    print test, maxsubseq(test)

    test = [10,4,3,15,5,6,7]
    print test, maxsubseq(test)


if __name__ == "__main__":
    test()
