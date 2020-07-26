from Chapter_4.Trees.BinaryNode import *
from Chapter_4.Trees.BinarySearchTree import *


class ValidateBST:

    def __init__(self):
        self.itIsBST = None

    def CheckIfItsBST(self, root):
        if root is None:
            return
        if root.leftNode is not None:
            checkLeft = root.leftNode.value < root.value
            if not checkLeft:
                self.itIsBST = False
                exit()
            else:
                self.itIsBST = True
                self.CheckIfItsBST(root.leftNode)
        if root.rightNode is not None:
            checkRight = root.rightNode.value > root.value
            if not checkRight:
                self.itIsBST = False
                exit()
            else:
                self.itIsBST = True
                self.CheckIfItsBST(root.rightNode)


BinarySearchTree = BinarySearchTree()
BinarySearchTree.mainRoot = BinaryNode(50)
root = BinarySearchTree.mainRoot
BinarySearchTree.Add(root, BinaryNode(55))
BinarySearchTree.Add(root, BinaryNode(60))
BinarySearchTree.Add(root, BinaryNode(65))
BinarySearchTree.Add(root, BinaryNode(70))

IsBST = ValidateBST()
IsBST.CheckIfItsBST(root)
result = IsBST.itIsBST
print("Is it BST? ---> ", result)
