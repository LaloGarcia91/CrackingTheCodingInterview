from Chapter_2.LinkedList import *


class SumLinkedLists:

    def PrepareListsToSum(self, list1, list2):
        if (list1.head is None) or (list2.head is None): return
        list1_size = list1.getListSize()
        list2_size = list2.getListSize()
        if list1_size > list2_size:
            for i in range(list1_size - list2_size):
                list2.append(0)
        if list2_size > list1_size:
            for i in range(list2_size - list1_size):
                list1.append(0)
        sumedNumberResult = self.GetSummedListsNumber(list1, list2)
        self.PrintSummedListResult(sumedNumberResult)

    def GetSummedListsNumber(self, list1, list2):
        currentNode_1 = list1.head
        currentNode_2 = list2.head
        acumulate = 0
        while currentNode_1 is not None:
            nodesSum = int(currentNode_1.data) + int(currentNode_2.data)
            currentNode_1 = currentNode_1.nextNode
            currentNode_2 = currentNode_2.nextNode
            acumulate += nodesSum
        return acumulate

    def PrintSummedListResult(self, result):
        sumedListResult = LinkedList()
        resultAsAstr = list(str(result))
        for result in resultAsAstr:
            sumedListResult.append(result)
        sumedListResult.printList()


list1 = LinkedList()
list1.append(99)
list1.append(2)
list1.append(4)

list2 = LinkedList()
list2.append(26)
list2.append(3)
list2.append(6)

SumLinkedLists().PrepareListsToSum(list1, list2)
