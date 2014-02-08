import random

def overlap(inp):
    earliest_end = 9999
    latest_beg = 0
    for start, end in inp:
        earliest_end = min(end, earliest_end)
        latest_beg = max(latest_beg, start)
    if earliest_end - latest_beg + 1 > 2:
        return (latest_beg, latest_beg+1)
    else:
        return (earliest_end-1, latest_beg+1)
        
if __name__ == "__main__":
    arr = [(1,3), (4,6), (9,10)]
    print arr, overlap(arr)

    arr = [(1,5), (1,4)]
    print arr, overlap(arr)
