#!/usr/bin/python
from __future__ import print_function
import random
from collections import *
LEFT, RIGHT, VAL = 0, 1, 2

def _inorder(node, lam):
    if not node: return
    LEFT, RIGHT, VAL = 0, 1, 2
    if node[LEFT]: _inorder(node[LEFT], lam)
    lam(node[VAL])
    if node[RIGHT]: _inorder(node[RIGHT], lam)

def queueleft(node,dq):
    while node:
        dq.append(node)
        node = node[LEFT]
    

def _inorder2(node, lam):
    dq = deque()
    queueleft(node, dq)
    while len(dq):
        node = dq.popleft()
        lam(node[VAL])
        queueleft(node[RIGHT], dq)
        
    
    

class Tree(object):
    LEFT, RIGHT, VAL = 0, 1, 2
    def __init__(self):
        self.root = None
    def _ninsert(self,node, val):
        LEFT, RIGHT, VAL = 0, 1, 2
        if node[VAL] <= val:
            if node[LEFT]:       
                self._ninsert(node[LEFT],val)
            else:
                node[LEFT] = [None, None, val]
        else:
            if node[RIGHT]:
                self._ninsert(node[RIGHT], val)
            else:
                node[RIGHT] = [None, None, val]
        
    def insert(self, val):
        LEFT, RIGHT, VAL = 0, 1, 2
        if self.root:
            self._ninsert(self.root, val)
        else:
            self.root = [None, None, val]

           
    def inorder(self,lam):
        _inorder(self.root, lam)
    def inorder2(self,lam):
        _inorder2(self.root, lam)

    

tr = Tree()
for x in range(10):
    tr.insert(random.randint(0, 15))

print("recurse:")
tr.inorder(lambda arg: print(" {} ".format(arg)))
print("queue")
tr.inorder2(lambda arg: print(" {} ".format(arg)))


