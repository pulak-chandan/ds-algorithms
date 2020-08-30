import datastructures.linkedLists.src.singleLinkedList as singleLinkedList

'''
input:  10 -> 20 -> 30 -> 40 -> 50 -> -10 -> -20 -> -30 -> -40 -> -50
output: 10 -> -10 -> 20 -> -20 -> 30 -> -30 -> 40 -> -40 -> 50 -> -50
'''


def reorder():
    if not sll.isEmpty():
        slow = sll.head
        fast = sll.head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        fast = sll.head
        while slow:
            temp = slow
            slow = slow.next
            temp.next = fast.next
            fast.next = temp
            fast = temp.next
        temp.next = None


sll = singleLinkedList.LinkedList()
testData = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]

# create input linked list
'''
for _ in testData:
    # O(N)
    sll.insertEnd(_)
'''
for _ in testData[::-1]:
    # O(1)
    sll.insertStart(_)

reorder()
print("Output:")
sll.traverse()
