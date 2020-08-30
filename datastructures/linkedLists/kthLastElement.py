import datastructures.linkedLists.src.singleLinkedList as singleLinkedList


def findElementFromLast(k):
    if not sll.isEmpty():
        fast = sll.head
        for _ in range(0, k-1):
            fast = fast.next
        slow = sll.head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data


sll = singleLinkedList.LinkedList()
testData = [1, -1, 4, 0, 67, -1, 34, 67, -1, 22, 22, 100, 1, 98, 4, 67]
# create input linked list
for _ in testData[::-1]:
    # O(1)
    sll.insertStart(_)

print(findElementFromLast(int(input("Enter value for k:"))))