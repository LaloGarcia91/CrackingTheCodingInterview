from Chapter_3.MyStack import *


class ThreeInOne:
    maxNumberOfStacks = 3
    singleArrayStacks = []

    def __init__(self):
        self.createThreeStacksInSingleArray()

    def createThreeStacksInSingleArray(self):
        self.singleArrayStacks.append(MyStack())
        self.singleArrayStacks.append(MyStack())
        self.singleArrayStacks.append(MyStack())

    def getTheArrayOfStacks(self):
        if len(self.singleArrayStacks) != self.maxNumberOfStacks:
            return
        return self.singleArrayStacks

    def printTheThreeStacks(self):
        if len(self.singleArrayStacks) != self.maxNumberOfStacks:
            return
        stackNumber = 1
        for thisStack in self.singleArrayStacks:
            print("Stack # "+str(stackNumber))
            thisStack.printStack()
            stackNumber += 1


threeInOne = ThreeInOne()
arrayOfStacks = threeInOne.getTheArrayOfStacks()

# the stack 1 is the index 0 of the array of stacks
arrayOfStacks[0].push(1)
arrayOfStacks[0].push(2)
arrayOfStacks[0].push(3)

# the stack 2 is the index 1 of the array of stacks
arrayOfStacks[1].push(4)
arrayOfStacks[1].push(5)
arrayOfStacks[1].push(6)

# the stack 3 is the index 2 of the array of stacks
arrayOfStacks[2].push(7)
arrayOfStacks[2].push(8)
arrayOfStacks[2].push(9)

threeInOne.printTheThreeStacks()
