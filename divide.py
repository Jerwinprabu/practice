#!/usr/bin/python

""" implement division without integer divide """

a = 1000 
b = 19


divisor = b
dividend = a

res = 0
temp = dividend
for i in range(31, -1, -1):
    t = divisor << i
    if t <= temp:
        print i
        temp -= t
        res |= 1 << i
print res


def convertToArray(num):
    ret = []
    for x in range(11):
        ret.append(num % 10)
        num = num / 10 
    ret.reverse()
    return ret


print a/b
