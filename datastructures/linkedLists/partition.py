import datastructures.linkedLists.src.singleLinkedList as singleLinkedList


def partition(pivot):
    if not sll.isEmpty():
        prev = None
        temp = sll.head
        greaterSLL = singleLinkedList.LinkedList()
        while temp is not None:
            if temp.data >= pivot:
                greaterSLL.insertStart(temp.data)
                sll.deleteNode(prev, temp)
            else:
                prev = temp
            temp = temp.next
        prev.next = greaterSLL.head


sll = singleLinkedList.LinkedList()
testData = [1, -1, 4, 0, 67, -1, 34, 67, -1, 22, 22, 100, 1, 98, 4, 67, 13]
# create input linked list
for _ in testData[::-1]:
    # O(1)
    sll.insertStart(_)
partition(25)
sll.traverse()