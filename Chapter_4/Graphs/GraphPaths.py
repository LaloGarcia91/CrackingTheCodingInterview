# Python program to print all paths from a source to destination.
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class GraphPaths:

    def __init__(self):
        self.edgesNumber = 0
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, fromHere, toHere):
        self.graph[fromHere].append(toHere)
        self.edgesNumber += 1

    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''

    def printAllPathsUtil(self, fromHere, toHere, visited, path):
        visited[fromHere] = True
        path.append(fromHere)
        if fromHere == toHere:
            print(path)
        else:
            for i in self.graph[fromHere]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, toHere, visited, path)
        path.pop()
        visited[fromHere] = False


    def printAllPaths(self, fromHere, toHere):
        visited = [False] * self.edgesNumber
        path = []
        self.printAllPathsUtil(fromHere, toHere, visited, path)


g = GraphPaths()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

fromHere = 0
toHere = 3
print("Following are all different paths from %d to %d :" % (fromHere, toHere))
g.printAllPaths(fromHere, toHere)
# This code is contributed by Neelam Yadav
