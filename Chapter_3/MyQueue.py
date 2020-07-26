

class MyQueue:
    class QueueNode:
        data = None
        next = None

        def __init__(self, data):
            self.data = data

    first = None
    last = None
    size = 0

    def add(self, value):
        newNode = self.QueueNode(value)
        if self.last is not None:
            self.last.next = newNode
        self.last = newNode
        if self.first is None:
            self.first = self.last
        self.size += 1

    def remove(self):
        if self.first is None:
            self.last = None
            return
        data = self.first.data
        self.first = self.first.next
        self.size -= 1
        return data

    def peek(self):
        if self.first is None:
            return
        return self.first.data

    def is3(self):
        return self.first is None

    def printQueue(self):
        firstNodeSoFar = self.first
        print("----- Current Queue -----")
        while firstNodeSoFar is not None:
            print(firstNodeSoFar.data)
            firstNodeSoFar = firstNodeSoFar.next

    def NodeExist(self, value):
        firstNode = self.first
        while firstNode is not None:
            if firstNode.data is value:
                return True
            firstNode = firstNode.next
        return False
