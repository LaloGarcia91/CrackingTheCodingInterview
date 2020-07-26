from Chapter_4.Trees.BinarySearchTree import *


class FirstCommonAncestor:

    def __init__(self):
        self.p_nodeParents = list()
        self.q_nodeParents = list()

    def Find(self, root, p, q):
        if root is None:
            return
        if root.value == p:
            self.BuildListOfParents(root, self.p_nodeParents)
        if root.value == q:
            self.BuildListOfParents(root, self.q_nodeParents)
        self.Find(root.leftNode, p, q)
        self.Find(root.rightNode, p, q)

    def BuildListOfParents(self, node, listOfParents):
        if node is None:
            return
        listOfParents.append(node.value)
        self.BuildListOfParents(node.parent, listOfParents)

    def Result(self):
        if (len(self.p_nodeParents) == 0) or (self.q_nodeParents == 0):
            return
        commonAncestor = None
        for p_parent in self.p_nodeParents:
            for q_parent in self.q_nodeParents:
                if p_parent == q_parent:
                    commonAncestor = p_parent
                    break
            if commonAncestor is not None:
                break
        print("Common Ancestor is: ", commonAncestor)
        print("p parents = ", self.p_nodeParents)
        print("q parents = ", self.q_nodeParents)


BinarySearchTree = BinarySearchTree()
BinarySearchTree.mainRoot = BinaryNode(50)
root = BinarySearchTree.mainRoot
BinarySearchTree.Add(root, BinaryNode(48))
BinarySearchTree.Add(root, BinaryNode(70))
BinarySearchTree.Add(root, BinaryNode(30))
BinarySearchTree.Add(root, BinaryNode(65))
BinarySearchTree.Add(root, BinaryNode(90))
BinarySearchTree.Add(root, BinaryNode(20))
BinarySearchTree.Add(root, BinaryNode(32))
BinarySearchTree.Add(root, BinaryNode(67))
BinarySearchTree.Add(root, BinaryNode(98))
BinarySearchTree.Add(root, BinaryNode(15))
BinarySearchTree.Add(root, BinaryNode(25))
BinarySearchTree.Add(root, BinaryNode(31))
BinarySearchTree.Add(root, BinaryNode(35))
BinarySearchTree.Add(root, BinaryNode(66))
BinarySearchTree.Add(root, BinaryNode(69))
BinarySearchTree.Add(root, BinaryNode(94))
BinarySearchTree.Add(root, BinaryNode(99))

BinarySearchTree.GetRandomNode()

FirstCommonAncestor = FirstCommonAncestor()
FirstCommonAncestor.Find(root, 20, 32)
FirstCommonAncestor.Result()
