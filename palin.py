#!/usr/bin/python

class PalinDecorator(object):
    def __init__(self, fx):
        self.cache = {}
        self.fx = fx
    def __call__(self, n):
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = self.fx(n)
            return self.cache[n]
            
        
@PalinDecorator
def palindrome(n):
    print n
    if len(n) == 1:
        return (1, n)
    elif len(n) == 0:
        return (0, "")
    else:
        if n[0] == n[-1]:
            pal = palindrome(n[1:-1])
            return (pal[0]+2, n[0]+ pal[1] + n[-1])
        else:
            x, y = palindrome(n[1:]), palindrome(n[0:-1])
            return x if x[0] > y[0] else y
        

def test():
    palin = "character"
    print palin, palindrome(palin)

if __name__ == '__main__':
    test()
