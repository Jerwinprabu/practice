#!/usr/bin/python

def lookAndSay(n):
    i = 0
    while i < n:
        if i == 0:
            cur = str(1)
        else:
            count = 0
            prev = cur
            cur = str()
            prev_char = prev[0]
            #print "cur: {} prev: {}".format(cur, prev)

            for char in prev:
                if char == prev_char:
                    count+= 1
                else:
                    cur += str(count) + prev_char
                    prev_char = char
                    count = 1
            cur += str(count) + prev_char

        yield cur

        i+=1

def test():

    print "look and say"
    for i,seq in enumerate(lookAndSay(15)):
        print "itr: {} num: {}".format(i,seq)
if __name__ == '__main__':
    test()
    
