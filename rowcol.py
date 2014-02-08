#!/usr/bin/python

""" given a matrix of numbers in which some may be zero if a cell contains
    zero, set all the cells in the row and column to zero """
def setrow(mat,pos):
    for i in range(len(mat[pos[0]])):
        mat[pos[0]][i] = 0


def setrowcol(mat, pos):
    for i in range(len(mat)):
        mat[i][pos[1]] = 0
    for i in range(len(mat[pos[0]])):
        mat[pos[0]][i] = 0

def process(mat):
    i, j = 0, 0
    setcol = [False for x in mat[0]]
    while i < len(mat):
        j = 0
        while j < len(mat[0]):
            if mat[i][j] == 0 and not setcol[j]:
                setrowcol(mat,(i,j))
                i+=1
                setcol[j] = True
                break
            elif mat[i][j] == 0:
                setrow(mat, (i,j))
                i+=1
                break
            j+=1
        i+=1
                
matrix = [[0 for x in range(10)] for y in range(10)]
process(matrix)
print matrix

    
