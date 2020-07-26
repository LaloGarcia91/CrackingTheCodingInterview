class Graph:

    def __init__(self):
        self.graph = {}

    def AddEdge(self, newVertex, adjacentNodes):
        if self.VertexExistInGraph(newVertex):
            self.graph[newVertex] += adjacentNodes
            return
        self.graph[newVertex] = adjacentNodes

    def VertexExistInGraph(self, vertex):
        if vertex in self.graph:
            return True
        return False

    def GetGraphObj(self):
        return self.graph

    def PrintVertexWithChilds(self, vertex):
        print("Node: ", vertex, "----->", "Adjacent Nodes: ", self.graph[vertex])

    def PrintGraph(self):
        print("\n--- Complete Graph")
        for vertex in self.graph.keys():
            self.PrintVertexWithChilds(vertex)