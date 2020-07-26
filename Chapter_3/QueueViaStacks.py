from Chapter_3.MyStack import *
from Chapter_3.MyQueue import *


class QueueViaStacks:

    def createQueueFromThisStack(self, queue, stack):
        if stack.isEmpty():
            return
        stack = self.reversedStack(stack)
        self.addTheStackNodesToTheQueue(queue, stack)

    def reversedStack(self, stack):
        tempStack = MyStack()
        while not stack.isEmpty():
            tempStack.push(stack.pop())
        return tempStack

    def addTheStackNodesToTheQueue(self, queue, stack):
        addThisNode = stack.top
        while addThisNode is not None:
            queue.add(addThisNode.data)
            addThisNode = addThisNode.next


# the stack-1 that holds the nodes to create the queue
stack_1 = MyStack()
stack_1.push(1)
stack_1.push(2)
stack_1.push(3)
stack_1.printStack()

# an extra stack-2 that holds nodes to keep creating the same queue
stack_2 = MyStack()
stack_2.push(4)
stack_2.push(5)
stack_2.push(6)
stack_2.printStack()

# the queue that will be created by the stack nodes
thisQueue = MyQueue()

# the class that creates the final queue via the stack
queueFromStack = QueueViaStacks()
queueFromStack.createQueueFromThisStack(thisQueue, stack_1)
queueFromStack.createQueueFromThisStack(thisQueue, stack_2)

# the final queue printed
thisQueue.printQueue()
