#!/usr/bin/python
import random

""" Imagine a robot istting on the upper left ocern of a an X by Y grid.
    The robot can only move in two directions, right and down. How many
    possible paths can the robot take from (0,0) to (X, Y)"""

class Memoize(object):
    def __init__(self, fx):
        self.fx = fx
        self.init = False
        self.grid = None
    def __call__(self, gridSize):
        if self.init:
            if self.grid[gridSize[0]][gridSize[1]] == -1:
                self.grid[gridSize[0]][gridSize[1]] = self.fx(gridSize)
            return self.grid[gridSize[0]][gridSize[1]]
        else:
            self.init = True
            self.grid = [[-1 for y in range(gridSize[1]+1)] for x in range(gridSize[0]+1)]
            print "{},{}".format(len(self.grid), len(self.grid[0]))
            res = self.fx(gridSize)
            self.init = False
            del self.grid
            return res
        
@Memoize
def dumbPossiblePaths(gridSize):
    assert gridSize[0]
    assert gridSize[1]
    if gridSize[0] > 1 and gridSize[1] > 1:
        paths = dumbPossiblePaths((gridSize[0]-1,gridSize[1]))
        paths += dumbPossiblePaths((gridSize[0],gridSize[1]-1))
        return paths
    elif gridSize[0] == 1:
        return 1
    elif gridSize[1] == 1:
        return 1

def test():
    inp = [(random.randint(1,15),random.randint(1,15)) for x in range(10)]
    
    for pair in inp:
        print "x,y: {}, paths: {}".format(pair, dumbPossiblePaths(pair))

if __name__ == '__main__':
    test()
