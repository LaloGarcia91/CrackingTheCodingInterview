from Chapter_4.Trees.BinaryNode import *
from Chapter_2.LinkedList import *
import math


class ListOfDepths:

    def __init__(self):
        self.allListsOfDepths = []
        self.binaryTreeRoot = None

    def add(self, root, node):
        if node.value > root.value:
            if root.rightNode is None:
                root.rightNode = node
            else:
                self.add(root.rightNode, node)
        else:
            if root.leftNode is None:
                root.leftNode = node
            else:
                self.add(root.leftNode, node)

    def BuildListOfDepths(self):
        root = self.binaryTreeRoot
        if root is None:
            return
        current = LinkedList()
        current.append(root)
        while current.getListSize() > 0:
            self.allListsOfDepths.append(current)  # add the previous level
            parents = current  # go to next level
            current = LinkedList()

            currentParent = parents.head  # head of the linked list (holds a binary node)
            while currentParent is not None:
                node = currentParent.data
                if node.leftNode is not None:
                    current.append(node.leftNode)
                if node.rightNode is not None:
                    current.append(node.rightNode)
                currentParent = currentParent.nextNode

    def PrintListOfDepths(self):
        self.BuildListOfDepths()
        currentNode = None
        depth = 1
        for parent in self.allListsOfDepths:
            print("----------> Depth #", depth)
            currentNode = parent.head
            while currentNode is not None:
                print(currentNode.data.value)
                currentNode = currentNode.nextNode
            depth += 1


listOfDepths = ListOfDepths()
listOfDepths.binaryTreeRoot = BinaryNode(50)
root = listOfDepths.binaryTreeRoot
listOfDepths.add(root, BinaryNode(48))
listOfDepths.add(root, BinaryNode(67))
listOfDepths.add(root, BinaryNode(70))
listOfDepths.add(root, BinaryNode(30))
listOfDepths.add(root, BinaryNode(65))
listOfDepths.add(root, BinaryNode(90))
listOfDepths.add(root, BinaryNode(20))
listOfDepths.add(root, BinaryNode(32))
listOfDepths.add(root, BinaryNode(98))
listOfDepths.add(root, BinaryNode(15))
listOfDepths.add(root, BinaryNode(25))
listOfDepths.add(root, BinaryNode(31))
listOfDepths.add(root, BinaryNode(35))
listOfDepths.add(root, BinaryNode(66))
listOfDepths.add(root, BinaryNode(69))
listOfDepths.add(root, BinaryNode(94))
listOfDepths.add(root, BinaryNode(99))
listOfDepths.PrintListOfDepths()
