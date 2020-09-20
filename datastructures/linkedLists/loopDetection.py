import datastructures.linkedLists.src.singleLinkedList as singleLinkedList

def findLoopPoint(l1):
    

def createTestData():
    sll1 = singleLinkedList.LinkedList()
    testData1 = [1, -1, 4, 0, 67, -1, 34]
    # create input linked list
    for _ in testData1[::-1]:
        # O(1)
        sll1.insertStart(_)

    # corrupt the linked list
    loopPoint = sll1.head
    for _ in range(0, 4):
        loopPoint = loopPoint.next

    tail = sll1.head
    while tail.next is not None:
        tail = tail.next
    tail.next = loopPoint
    return sll1


l1 = createTestData()
findLoopPoint(l1)
