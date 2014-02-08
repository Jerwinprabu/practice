#!/usr/bin/python

def reverse(arr):
    if not arr: return
    i, j = 0, len(arr)-1
    while j > i:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return arr

def rotate(arr, n):
    a = arr[:]
    a = reverse(a)
    a[n:] = reverse(a[n:])
    a[:n] = reverse(a[:n])
    return a

def test():
    arr = [1,2,3,4,5]
    print arr, rotate(arr, 1)
    print arr, rotate(arr, 2)

if __name__ == "__main__":
    test()
