from Chapter_4.Trees.BinaryNode import BinaryNode
import random


class BinarySearchTree:

    def __init__(self):
        self.mainRoot = None
        self.size = 0

    def Add(self, root, node):
        if self.mainRoot is None:
            self.mainRoot = root
        if root is None:
            return
        self.InsertRightNode(root, node)
        self.InsertLeftNode(root, node)

    def InsertRightNode(self, root, node):
        if node.value > root.value:
            if root.rightNode is None:
                root.rightNode = node
                root.rightNode.parent = root
                self.size += 1
            else:
                self.Add(root.rightNode, node)

    def InsertLeftNode(self, root, node):
        if node.value < root.value:
            if root.leftNode is None:
                root.leftNode = node
                root.leftNode.parent = root
                self.size += 1
            else:
                self.Add(root.leftNode, node)

    def PrintInOrder(self, root):
        if root is None:
            return
        self.PrintInOrder(root.leftNode)
        print(root.value)
        self.PrintInOrder(root.rightNode)

    def PrintInPreOrder(self, root):
        if root is None:
            return
        print(root.value)
        self.PrintInPreOrder(root.leftNode)
        self.PrintInPreOrder(root.rightNode)

    def Find(self, root, value):
        if root is None:
            return
        if root.value == value:
            return root
        self.Find(root.leftNode, value)
        self.Find(root.rightNode, value)

    def Delete(self, root, valueToDelete):
        if root is None:
            return
        if root.value == valueToDelete:
            if root.value is not self.mainRoot.value:
                root.parent.rightNode = root.rightNode
                root.parent.leftNode = root.leftNode
                self.size -= 1
                return
        self.Delete(root.leftNode, valueToDelete)
        self.Delete(root.rightNode, valueToDelete)

    def GetRandomNode(self):
        allNodes = list()
        self.ReturnARandomNode(self.mainRoot, allNodes)
        randomIndex = random.randint(0, self.size)
        randomNode = allNodes[randomIndex]
        print("Random node: ", randomNode)
        return randomNode

    def ReturnARandomNode(self, root, allNodes):
        if root is None:
            return
        allNodes.append(root.value)
        self.ReturnARandomNode(root.leftNode, allNodes)
        self.ReturnARandomNode(root.rightNode, allNodes)


