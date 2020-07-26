import math


class Node:
    data = None
    nextNode = None

    def __init__(self, data):
        self.data = data


class LinkedList:
    head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        currentNode = self.head
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = Node(data)

    def prepend(self, data):
        newHead = Node(data)  # in order to prepend a node, we need to create a new head
        newHead.nextNode = self.head # the old head is the NEXT node of the new head, meaning it will be index 1 of the list
        self.head = newHead  # set the new head of the linked list

    def deleteNode(self, deleteBy, thisValue):
        # a node can be deleted either by the node-value or by the index of the node in the linked list
        if self.head is None:
            return
        currentNode = self.head
        if deleteBy == "index":
            self.deleteNodeByIndex(currentNode, thisValue)
        if deleteBy == "value":
            self.deleteNodeByValue(currentNode, thisValue)
        if currentNode is None:
            print("The node " + deleteBy + ": " + str(thisValue) + " does NOT exist.")
            return
        self.printDeletedNodeMsg(deleteBy, thisValue)

    def deleteNodeByIndex(self, currentNode, thisIndex):
        if thisIndex == 0:
            self.head = self.head.nextNode
            return
        index = 0
        previousNode = None
        while index < thisIndex:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            index += 1
        previousNode.nextNode = currentNode.nextNode

    def deleteNodeByValue(self, currentNode, thisValue):
        previousNode = None
        while (currentNode.nextNode is not None) and currentNode.data != thisValue:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        previousNode.nextNode = currentNode.nextNode

    def printDeletedNodeMsg(self, msgType, thisData):
        if msgType == "index":
            print("..........deleted the node at index: " + str(thisData))
            return
        if msgType == "value":
            print("..........deleted the node with value of: " + str(thisData))
            return
        return False

    def getListSize(self):
        if self.head is None:
            return 0  # list size is 0
        currentNode = self.head  # the actual CURRENT node at this point of the program
        size = 1  # starts at 1, because we are counting the currentNode
        while currentNode.nextNode is not None:  # while the "currentNode" node in iteration is not the last node in the singled list
            currentNode = currentNode.nextNode
            size += 1
        return size

    def printListSize(self):
        print("..........current linked list size is: ", self.getListSize())

    def printList(self):
        print("..........CURRENT LIST BELOW")
        if self.head is None:
            print("There is nothing in the list.")
            return
        currentNode = self.head  # the current node (the first on the list)
        print("Node Index 0 => " + str(currentNode.data))
        index = 1  # start counting at index 1
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
            print("Node Index " + str(index) + " => " + str(currentNode.data))
            index += 1

    def replaceListNodesWithAnotherListNodes(self, thisList):
        currentNode_originalList = self.head
        currentNode_tempList = thisList.head
        while currentNode_originalList is not None:
            currentNode_originalList.data = currentNode_tempList.data
            currentNode_originalList = currentNode_originalList.nextNode
            currentNode_tempList = currentNode_tempList.nextNode

    def howManyTimesThisNodeRepeats(self, nodeValue):
        if self.head is None: return
        currentNode = self.head
        times = 0
        while currentNode is not None:
            if currentNode.data == nodeValue:
                times += 1
            currentNode = currentNode.nextNode
        return times

    def cloneOriginalListAsBackwards(self):
        originalListBackwards = LinkedList()
        currentNode = self.head
        originalListBackwards.prepend(currentNode)
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
            originalListBackwards.prepend(currentNode.data)
        return originalListBackwards

    def checkIfThis2NodesDataAreEqual(self, nodeData1, nodeData2):
        if nodeData1 == nodeData2: return True
        return False

    def deleteMiddleNodeFromList(self, linkedList):
        listSize = linkedList.getListSize()
        if listSize <= 2:
            return
        nodeIndex = math.floor((listSize - 1) / 2)
        linkedList.deleteNode("index", nodeIndex)

    def listPartition(self, linkedList, number):
        if linkedList.head is None:
            print("List is empty.")
            return
        tempList = LinkedList()
        currentNode_originalList = linkedList.head
        while currentNode_originalList is not None:
            if currentNode_originalList.data >= number:
                tempList.append(currentNode_originalList.data)
            else:
                tempList.prepend(currentNode_originalList.data)
            currentNode_originalList = currentNode_originalList.nextNode
        linkedList.replaceListNodesWithAnotherListNodes(tempList)

    def checkIfListIsPalindrome(self, linkedList):
        if linkedList.head is None:
            return
        originalListBackwards = linkedList.cloneOriginalListAsBackwards()

        backwardsListCurrentNode = originalListBackwards.head
        originalListCurrentNode = linkedList.head
        while originalListCurrentNode.nextNode is not None:
            if not linkedList.checkIfThis2NodesDataAreEqual(backwardsListCurrentNode.data,
                                                            originalListCurrentNode.data):
                print("List is NOT a palindrome.")
                return False
            originalListCurrentNode = originalListCurrentNode.nextNode
            backwardsListCurrentNode = backwardsListCurrentNode.nextNode
        print("List IS a palindrome.")
        return True

    def removeDuplicates(self):
        if self.head is None: return
        currentNode = self.head
        index = 0
        duplicatesFound = False
        while currentNode.nextNode is not None:
            if self.howManyTimesThisNodeRepeats(currentNode.data) > 1:
                self.deleteNode("value", currentNode.data)
                duplicatesFound = True
            currentNode = currentNode.nextNode
            index += 1
        if duplicatesFound is False:
            print("No duplicates were found")

    def printKthToLast(self, linkedList, kth):
        listSize = linkedList.getListSize()
        if linkedList.head is None:
            return False
        if kth > listSize:
            print("The Kth passed is longer than the linked list size.")
            return False
        getNodeAtThisIndex = listSize - kth
        currentNode = linkedList.head
        if kth == listSize:
            nodeValueMsg = "Value is: " + str(currentNode.data)
            nodeKthMsg = "Node at Kth: " + str(kth)
            print(nodeKthMsg + " | " + nodeValueMsg)
            return
        positionCounter = 1
        while positionCounter is not getNodeAtThisIndex:
            currentNode = currentNode.nextNode
            positionCounter += 1
        nodeValueMsg = "Value is: " + str(currentNode.nextNode.data)
        nodeKthMsg = "Node at Kth: " + str(kth)
        print(nodeKthMsg + " | " + nodeValueMsg)

    def returnKtnNode(self, linkedList, kth):
        listSize = linkedList.getListSize()
        if kth > listSize:
            return False
        currentNode = linkedList.head
        if kth == listSize:
            return currentNode
        positionCounter = 1
        while positionCounter is not (listSize - kth):
            currentNode = currentNode.nextNode
            positionCounter += 1
        return currentNode.nextNode

    def RemoveFirstNode(self):
        if self.head is None:
            return
        data = self.head.data
        self.head = self.head.nextNode
        return data
