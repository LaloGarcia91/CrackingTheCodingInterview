from Chapter_4.Trees.BinaryNode import BinaryNode
import math


class MinimalTree:

    def __init__(self):
        self.sortedArray = []
        self.rightSide = []
        self.leftSide = []

    def BuildTree(self, root):
        nodesToCreateTree = self.leftSide + self.rightSide
        for element in nodesToCreateTree:
            node = BinaryNode(element)
            self.InsertToRight(root, node)
            self.InsertToLeft(root, node)

    def InsertToRight(self, root, node):
        middleNodeValue = self.FindMiddleElement()
        if node.value > middleNodeValue:
            #print("Node value: ", node.value, " > ", " Main Root value: ", middleNodeValue)
            if root.rightNode is None:
                root.rightNode = node
            else:
                self.InsertToLeft(root.rightNode, node)
                self.InsertToRight(root.rightNode, node)

    def InsertToLeft(self, root, node):
        middleNodeValue = self.FindMiddleElement()
        if node.value < middleNodeValue:
            if root.leftNode is None:
                root.leftNode = node
            else:
                self.InsertToLeft(root.leftNode, node)
                self.InsertToRight(root.leftNode, node)

    def SplitRightAndLeftSides(self):
        middle = self.FindMiddleElement()
        indexOfMiddle = self.sortedArray.index(middle)
        self.leftSide = self.sortedArray[0:indexOfMiddle]
        self.rightSide = self.sortedArray[(indexOfMiddle + 1):len(self.sortedArray)]

    def FindMiddleElement(self):
        middle = int(len(self.sortedArray)) / 2
        if middle % 2 != 0:
            return math.ceil(middle)
        return round(middle)

    def PrintTree(self, root):
        if root is None:
            return
        print(root.value)
        self.PrintTree(root.leftNode)
        self.PrintTree(root.rightNode)


minimalTree = MinimalTree()
minimalTree.sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
minimalTree.SplitRightAndLeftSides()

root = BinaryNode(minimalTree.FindMiddleElement())
minimalTree.BuildTree(root)
minimalTree.PrintTree(root)
