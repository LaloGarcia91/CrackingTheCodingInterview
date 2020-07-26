class MyStack:
    class StackNode:
        data = None
        next = None

        def __init__(self, thisData):
            self.data = thisData

    top = None
    nodesSoFar = 0
    minValueSoFar = None

    def pop(self):
        if self.top is None:
            return
        value = self.top.data
        self.top = self.top.next
        self.nodesSoFar -= 1
        return value

    def push(self, value):
        node = self.StackNode(value)
        node.next = self.top
        self.top = node
        self.nodesSoFar += 1

    def peek(self):
        if self.top is None:
            return
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def sortStack(self):
        tempStack = MyStack()
        while self.isEmpty() is False:
            popped = self.pop()
            while (tempStack.isEmpty() is False) and (tempStack.peek() > popped):
                self.push(tempStack.pop())
            tempStack.push(popped)
        while tempStack.isEmpty() is False:
            self.push(tempStack.pop())
        self.printStack()

    def printStack(self):
        if self.isEmpty():
            print("Empty Stack.")
            return
        currentNode = self.top
        print("----- Current Stack -----")
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
