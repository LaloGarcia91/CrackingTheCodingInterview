from Chapter_4.Trees.BinarySearchTree import *


class PathsWithSum:

    def __init__(self):
        self.paths = None
        self.totalPaths = None

    def CountPathsWithSum(self, root, targetSum):
        if root is None:
            return 0
        # count paths with sum starting from the root
        pathsFromRoot = self.CountPathsWithSumFromNode(root, targetSum, 0)
        # try the nodes on the left and right
        pathsOnLeft = self.CountPathsWithSum(root.leftNode, targetSum)
        pathsOnRight = self.CountPathsWithSum(root.rightNode, targetSum)
        if (pathsFromRoot is not None) and (pathsOnLeft is not None) and (pathsOnRight is not None):
            self.paths = pathsFromRoot + pathsOnLeft + pathsOnRight

    # returns the number of paths with this sum starting from this node
    def CountPathsWithSumFromNode(self, node, targetSum, currentSum):
        if node is None:
            return 0
        currentSum += node.value
        self.totalPaths = 0
        if currentSum == targetSum:
            # found a path from the root
            self.totalPaths += 1
        self.totalPaths += self.CountPathsWithSumFromNode(node.leftNode, targetSum, currentSum)
        self.totalPaths += self.CountPathsWithSumFromNode(node.rightNode, targetSum, currentSum)
        return self.totalPaths


BinarySearchTree = BinarySearchTree()
BinarySearchTree.mainRoot = BinaryNode(10)
root = BinarySearchTree.mainRoot
BinarySearchTree.Add(root, BinaryNode(5))
BinarySearchTree.Add(root, BinaryNode(-3))
BinarySearchTree.Add(root, BinaryNode(3))
BinarySearchTree.Add(root, BinaryNode(2))
BinarySearchTree.Add(root, BinaryNode(11))
BinarySearchTree.Add(root, BinaryNode(3))
BinarySearchTree.Add(root, BinaryNode(-2))
BinarySearchTree.Add(root, BinaryNode(1))

PathsWithSum = PathsWithSum()
PathsWithSum.CountPathsWithSum(root, 8)
print(PathsWithSum.paths)
