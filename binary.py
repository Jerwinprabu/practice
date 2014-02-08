#!/usr/bin/python

import random

class BinaryNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.rchild = None
        self.lchild = None

class BinaryTree(object):
    def __init__(self):
        self.root = None
    def __getitem__(self, key):
        found = False
        node = self.root
        while node:
            if node.key == key:
                break
            elif node.key < key:
                node = node.lchild
            elif node.key > key:
                node = node.rchild
        if node: return node.value
        else: return None
        
    def __setitem__(self, key, value):
        nnode = BinaryNode(key, value)
        node = self.root

        if not node:
            self.root = nnode

        while node:
            if node.value == value:
                break
            elif key < node.value:
                if node.lchild:
                    node = node.lchild
                else:
                    node.lchild = nnode
                    break
            elif key > node.value:
                if node.rchild:
                    node = node.rchild
                else:
                    node.rchild = nnode
                    break
    def pretty_print(self):
        nlist = list()
        nlist.append(self.root)
        level = 0

        while len(nlist):
            nlevel = list()
            print "level {}".format(level) ,
            while len(nlist):
                n = nlist.pop(0)
                print (n.key, n.value),
                if n.lchild: nlevel.append(n.lchild)
                if n.rchild: nlevel.append(n.rchild)
            level +=1
            nlist = nlevel
            print
        
def test():
    randarray = [random.randint(0, 1000) for x in range(50)]
    tree = BinaryTree()
    for num in randarray:
        tree[num] = num
    tree.pretty_print()
        
            
if __name__ == '__main__':
    test()
