from Chapter_2.LinkedList import *
from Chapter_4.Trees.BinarySearchTree import *


class CheckBalanced:

    def __init__(self):
        self.BST = BinarySearchTree()
        self.root = BinaryNode(50)
        self.theTreeIsBalanced = False

    def IsBalanced(self, root):
        if root is None:
            return
        heightDifference = abs(self.GetHeight(root.leftNode) - self.GetHeight(root.rightNode))
        if heightDifference > 1:
            self.theTreeIsBalanced = False
        else:
            self.theTreeIsBalanced = True  # this line NEEDS to be the first line in this statement
            self.IsBalanced(root.leftNode)
            self.IsBalanced(root.rightNode)

    def GetHeight(self, root):
        if root is None:
            return -1
        childsCount = 0
        if root.leftNode is not None:
            childsCount += 1
        if root.rightNode is not None:
            childsCount += 1
        return childsCount

    def PrintResult(self):
        if self.theTreeIsBalanced:
            print("Balanced Tree.")
        else:
            print("Not Balanced Tree.")

    def TestWithBalancedTree(self):
        self.BST.Add(self.root, BinaryNode(17))
        self.BST.Add(self.root, BinaryNode(72))
        self.BST.Add(self.root, BinaryNode(12))
        self.BST.Add(self.root, BinaryNode(23))
        self.BST.Add(self.root, BinaryNode(54))
        self.BST.Add(self.root, BinaryNode(76))
        self.BST.Add(self.root, BinaryNode(9))
        self.BST.Add(self.root, BinaryNode(14))
        self.BST.Add(self.root, BinaryNode(19))
        self.BST.Add(self.root, BinaryNode(67))

    def TestWithUnbalancedTree(self):
        self.BST.Add(self.root, BinaryNode(17))
        self.BST.Add(self.root, BinaryNode(76))
        self.BST.Add(self.root, BinaryNode(9))
        self.BST.Add(self.root, BinaryNode(23))
        self.BST.Add(self.root, BinaryNode(54))
        self.BST.Add(self.root, BinaryNode(14))
        self.BST.Add(self.root, BinaryNode(19))
        self.BST.Add(self.root, BinaryNode(72))
        self.BST.Add(self.root, BinaryNode(12))
        self.BST.Add(self.root, BinaryNode(67))


CheckBalanced = CheckBalanced()
CheckBalanced.TestWithBalancedTree()
# CheckBalanced.TestWithUnbalancedTree()
CheckBalanced.IsBalanced(CheckBalanced.root)
CheckBalanced.PrintResult()
