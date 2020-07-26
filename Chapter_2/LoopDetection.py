from Chapter_2.LinkedList import *


class LinkedListLoopDetect:

    def FindBeginning(self, linkedList):
        slow = linkedList.head
        fast = linkedList.head

        # find meeting point. This will be LOOP_SIZE - k steps into the linked list
        while fast is not None and fast.nextNode is not None:
            slow = slow.nextNode
            fast = fast.nextNode.nextNode
            if slow == fast:  # collision
               break

        # Error checking - no meeting point, and therefore no loop
        if fast is None or fast.nextNode is None:
            return None

        '''
        Move slow to head. Keep fast at Meeting point. Each are k steps from the Loop Start.
        If they move at the same pace, they must meet at Loop Start.
        '''
        slow = linkedList.head
        while slow != fast:
            slow = slow.nextNode
            fast = fast.nextNode
        # Both now point to the start of the loop
        return fast


llist = LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("C")
llist.printList()

result = LinkedListLoopDetect().FindBeginning(llist)
print(result)
