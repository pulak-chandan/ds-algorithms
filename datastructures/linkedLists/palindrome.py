import datastructures.linkedLists.src.singleLinkedList as singleLinkedList

'''
LIFOQueue is the stack implementation in Python. 
We can also use collections.dequeue 
or 
We can implement our own Stack
'''
from queue import LifoQueue


def checkPalindrome():
    if not sll.isEmpty():
        stack = LifoQueue()
        fast = slow = sll.head
        stack.put(slow.data)
        while fast.next and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            stack.put(slow.data)
        slow = slow.next

        # length is odd, remove middle element. If length is even then fast.next.next will be None
        if fast.next is None:
            stack.get()

        while slow is not None:
            if slow.data != stack.get():
                return False
            slow = slow.next
        return True


sll = singleLinkedList.LinkedList()
testData = [1, 0, 7, 9, 7, 0, 1]
# create input linked list
for _ in testData[::-1]:
    # O(1)
    sll.insertStart(_)
print(checkPalindrome())