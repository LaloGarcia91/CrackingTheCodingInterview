from Chapter_4.Trees.BinarySearchTree import *


class Successor:

    def __init__(self):
        self.closestSuccessorValue = None
        self.nodeValueToCheck = None

    def Check(self, root):
        if root is None:
            return
        if root.value > self.nodeValueToCheck:
            if self.closestSuccessorValue is None:
                self.closestSuccessorValue = root.value
            if root.value < self.closestSuccessorValue:
                self.closestSuccessorValue = root.value
        self.Check(root.leftNode)
        self.Check(root.rightNode)

    def PrintResult(self):
        print("Node value to check: ", self.nodeValueToCheck)
        print("Closest Successor: ", self.closestSuccessorValue)


BinarySearchTree = BinarySearchTree()
BinarySearchTree.mainRoot = BinaryNode(50)
root = BinarySearchTree.mainRoot
BinarySearchTree.Add(root, BinaryNode(60))
BinarySearchTree.Add(root, BinaryNode(79))
BinarySearchTree.Add(root, BinaryNode(65))
BinarySearchTree.Add(root, BinaryNode(67))
BinarySearchTree.Add(root, BinaryNode(78))
BinarySearchTree.Add(root, BinaryNode(53))
BinarySearchTree.Add(root, BinaryNode(99))
BinarySearchTree.Add(root, BinaryNode(51))
BinarySearchTree.Add(root, BinaryNode(82))

Successor = Successor()
Successor.nodeValueToCheck = 78
Successor.Check(root)
Successor.PrintResult()
