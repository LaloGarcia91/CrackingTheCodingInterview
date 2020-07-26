from Chapter_3.MyQueue import *
from Chapter_4.Graphs.Graph import *


class GraphBFS:

    def __init__(self):
        self.graph = None  # receive the graph object
        self.visitedNodes = MyQueue()
        self.enqueuedNodes = MyQueue()
        self.lastVertexEnqueued = None

    def BFS(self, root):
        self.enqueuedNodes.add(root)
        self.visitedNodes.add(root)
        while self.enqueuedNodes.size > 0:
            self.lastVertexEnqueued = self.enqueuedNodes.remove()
            self.StartVisitingAdjacentNodesAndEnqueueThem()
            #print(self.lastVertexEnqueued)

    def StartVisitingAdjacentNodesAndEnqueueThem(self):
        for adjacentNode in self.graph[self.lastVertexEnqueued]:
            if not self.visitedNodes.NodeExist(adjacentNode):
                self.visitedNodes.add(adjacentNode)
                self.enqueuedNodes.add(adjacentNode)



graph = Graph()
graph.AddEdge(0, [4, 2, 0])
graph.AddEdge(2, [3, 0])
graph.AddEdge(3, [4])
graph.AddEdge(1, [2])
graph.AddEdge(4, [2, 0, 1])
graph.PrintGraph()

print("\n----- Breadth First Search -----")
bfs = GraphBFS()
bfs.graph = graph.GetGraphObj()
bfs.BFS(0)
