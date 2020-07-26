from Chapter_3.MyQueue import *
from Chapter_4.Graphs.Graph import *


class RouteBetweenNodes:

    def __init__(self):
        self.graph = None  # receive the graph object
        self.visitedNodes = list()
        self.tempRoute = list()
        self.allRoutes = list()
        self.startNode = None
        self.endNode = None

    def FindExistingRoutesBFS(self):
        self.visitedNodes.append(self.startNode)
        self.tempRoute.append(self.startNode)
        if self.startNode == self.endNode:
            self.AppendTempRouteToAllRoutes()
        else:
            self.StartVisitingAdjacentNodesAndUseRecursion()
        self.tempRoute.pop()
        self.visitedNodes.pop()

    def AppendTempRouteToAllRoutes(self):
        currentPath = list()
        for node in self.tempRoute:
            currentPath.append(node)
        self.allRoutes.append(currentPath)

    def StartVisitingAdjacentNodesAndUseRecursion(self):
        for adjacentNode in self.graph[self.startNode]:
            if adjacentNode not in self.visitedNodes:
                self.startNode = adjacentNode
                self.FindExistingRoutesBFS()

    def PrintRoutes(self):
        print("Routes:")
        for route in self.allRoutes:
            print(route)


graph = Graph()
graph.AddEdge(0, [1, 3, 4])
graph.AddEdge(1, [2, 0, 3])
graph.AddEdge(2, [1, 0, 4])
graph.AddEdge(3, [1, 2, 0])
graph.AddEdge(4, [2, 1, 0])
# graph.PrintGraph()

_routes = RouteBetweenNodes()
_routes.graph = graph.GetGraphObj()
_routes.startNode = 4
_routes.endNode = 0
_routes.FindExistingRoutesBFS()
_routes.PrintRoutes()
