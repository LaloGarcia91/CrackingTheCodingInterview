from Chapter_3.MyStack import *


class SetOfStacks:
    stacksSoFar = []
    maxStackLengthAllowed = 5

    def __init__(self):
        # append the first stack to the empty array that will hold O(n) stacks
        self.stacksSoFar.append(MyStack())

    def push(self, value):
        if self.stacksSoFar[-1].nodesSoFar == self.maxStackLengthAllowed:
            self.stacksSoFar.append(MyStack())
        self.stacksSoFar[-1].push(value)

    def pop(self):
        print("\n.......................POPPED --------> " + str(self.stacksSoFar[-1].pop()))
        if self.stacksSoFar[-1].nodesSoFar == 0:
            self.stacksSoFar.pop()

    def printStacks(self):
        print(" \n.......... PRINTING STACKS ..........\n")
        index = 0
        for stack in self.stacksSoFar:
            print("----- Stack # " + str(index + 1))
            stack.printStack()
            index += 1


allStacks = SetOfStacks()
allStacks.push(1)
allStacks.push(2)
allStacks.push(3)
allStacks.push(4)
allStacks.push(5)
allStacks.push(6)
allStacks.push(7)
allStacks.push(8)
allStacks.push(9)
allStacks.push(10)
allStacks.push(11)
allStacks.push(12)
allStacks.push(13)
allStacks.push(14)
allStacks.push(15)
allStacks.push(16)
allStacks.push(17)

allStacks.printStacks()
allStacks.pop()
allStacks.printStacks()
