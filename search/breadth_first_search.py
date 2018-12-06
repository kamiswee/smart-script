"""
    Breadth First Search is a graph traversal.  It is used to find
    the shortest path of a given graph as long as the graph does not
    contain loops, edges
"""
from collections import deque

class Vertex(object):

    def __init__(self, data=None):
        self.visited = False
        self.data = data


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

graph = {
    '(8,0,0)':['(5,3,0)','(3,0,5)'],
    '(5,3,0)':['(5,0,3)'],
    '(5,0,3)':['(2,3,3)'],
    '(2,3,3)':['(2,1,5)'],
    '(2,1,5)':['(7,1,0)'],
    '(7,1,0)':['(7,0,1)'],
    '(7,0,1)':['(4,3,1)'],
    '(4,3,1)':['4,0,4'],
    '(3,0,5)':['(3,3,2)'],
    '(3,3,2)':['(6,0,2)'],
    '(6,0,2)':['(6,2,0)'],
    '(6,2,0)':['(1,2,5)'],
    '(1,2,5)':['(1,3,4)'],
}
