from Chapter_4.Trees.BinarySearchTree import *


class CheckSubtree:

    def __init__(self):
        self.T1 = None
        self.T2 = None
        self.isSubtree = False
        self.t1AsStr = ""
        self.t2AsStr = ""

    def ContainsTree(self, t1Root, t2Root):
        self.GetOrderStringT1(t1Root)
        self.GetOrderStringT2(t2Root)
        if self.t2AsStr in self.t1AsStr:
            self.isSubtree = True
        else:
            self.isSubtree = False

    def GetOrderStringT1(self, root):
        if root is None:
            return
        self.t1AsStr += str(root.value) + " "
        self.GetOrderStringT1(root.leftNode)
        self.GetOrderStringT1(root.rightNode)

    def GetOrderStringT2(self, root):
        if root is None:
            return
        self.t2AsStr += str(root.value) + " "
        self.GetOrderStringT2(root.leftNode)
        self.GetOrderStringT2(root.rightNode)

    def Result(self):
        print("T1 = ", self.t1AsStr)
        print("T2 = ", self.t2AsStr)
        print("\nIs T2 a subtree of T1? --> ", self.isSubtree)


T1 = BinarySearchTree()
T1.mainRoot = BinaryNode(50)
T1.Add(T1.mainRoot, BinaryNode(17))
T1.Add(T1.mainRoot, BinaryNode(72))
T1.Add(T1.mainRoot, BinaryNode(12))
T1.Add(T1.mainRoot, BinaryNode(23))
T1.Add(T1.mainRoot, BinaryNode(54))
T1.Add(T1.mainRoot, BinaryNode(76))
T1.Add(T1.mainRoot, BinaryNode(9))
T1.Add(T1.mainRoot, BinaryNode(14))
T1.Add(T1.mainRoot, BinaryNode(15))
T1.Add(T1.mainRoot, BinaryNode(19))
T1.Add(T1.mainRoot, BinaryNode(67))

T2 = BinarySearchTree()
T2.mainRoot = BinaryNode(12)
T2.Add(T2.mainRoot, BinaryNode(9))
T2.Add(T2.mainRoot, BinaryNode(14))
T2.Add(T2.mainRoot, BinaryNode(15))

CheckSubtree = CheckSubtree()
CheckSubtree.T1 = T1.mainRoot
CheckSubtree.T2 = T2.mainRoot
CheckSubtree.ContainsTree(T1.mainRoot, T2.mainRoot)
CheckSubtree.Result()
