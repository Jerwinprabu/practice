#!/usr/bin/python

def comb(arr, n):
    if n == 0:
        yield []
    else:
        if len(arr) == 1:
            assert n == 1
            yield arr
        else:
            for i in range(0,len(arr)-n+1):
                for c in comb(arr[i+1:], n-1):
                    yield [arr[i]] + c
def test():
    a = [1,2,3,4,5]
    print a, len([c for c in comb(a,3)])
    print a, len([c for c in comb(a,2)])

if __name__ == '__main__':
    test()
