from Chapter_2.LinkedList import *


class LinkedListIntersection:

    def getIntersectionNode(self, list1, list2):
        head_1 = list1.head
        head_2 = list2.head
        if (not head_1) or (not head_2): return

        print(" ")
        print("----------- Making lists equal sizes ------------")
        self.makeBothListsEqualSizeIfNeeded(list1, list2)

        currentNode_1 = list1.head
        currentNode_2 = list2.head
        index = 0
        intersectionExist = False

        print(" ")
        print("----------- Looking for intersections ------------")
        while currentNode_1 is not None:
            if currentNode_1.data == currentNode_2.data:
                intersectionExist = True
                print("Intersecting node is: " + str(currentNode_1.data) + " --- At index: "+str(index)+" in both lists.")
            currentNode_1 = currentNode_1.nextNode
            currentNode_2 = currentNode_2.nextNode
            index += 1
        if not intersectionExist: print("There are no intersections.")

    def makeBothListsEqualSizeIfNeeded(self, list1, list2):
        list1_size = list1.getListSize()
        list2_size = list2.getListSize()

        if list1_size > list2_size:
            difference = list1_size - list2_size
            self.removeCharactersFromHeadOfLinkedList(difference, list1)
        if list2_size > list1_size:
            difference = list2_size - list1_size
            self.removeCharactersFromHeadOfLinkedList(difference, list2)

    def removeCharactersFromHeadOfLinkedList(self, howManyCharsToRemove, thisList):
        for i in range(howManyCharsToRemove):
            thisList.deleteNode("index", 0)


llist_1 = LinkedList()
llist_1.append(1)
llist_1.append(2)
llist_1.append(45)
llist_1.append(532)
llist_1.printList()

llist_2 = LinkedList()
llist_2.append(13)
llist_2.append(27)
llist_2.append(555)
llist_2.append(4)
llist_2.append(5)
llist_2.append(45)
llist_2.append(532)
llist_2.printList()

LinkedListIntersection().getIntersectionNode(llist_1, llist_2)
