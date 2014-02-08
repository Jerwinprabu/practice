#!/usr/bin/python

class Vertex(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def getName(self):
        return self.name    

class Edge(object):
    def __init__(self, src, dst, weight=5):
        self.src = src
        self.dst = dst
        self.weight = weight
    def __str__(self):
        return "{} -> {}".format(self.src.getName(), self.dst.getName())
    def getSrc(self):
        return self.src
    def getDst(self):
        return self.dst

class Graph(object):
    def __init__(self):
        self.edges = {}
        self.nodes = set()
    def addVertex(self, node):
        if node.getName() in nodes:
            raise ValueError("Node already exists")
        self.edges[node] = []
        self.nodes.add(node)
    def addEdge(self, edge):
        if edge.getSrc() not in self.nodes:
            raise ValueError("src node not real")
        if edge.getDst() not in self.nodes:
            raise ValueError("dst node not real")
        self.edges[edge.getSrc()].append(edge.getDst())

def test():
    pass

if __name__ == "__main__":
    test()
