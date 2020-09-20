import datastructures.linkedLists.src.singleLinkedList as singleLinkedList


def findIntersectionNode(l1, l2, s1, s2):
    temp1 = l1.head
    temp2 = l2.head
    if s1 > s2:
        for _ in range(0 , s1 - s2):
            temp1 = temp1.next
    elif s2 > s1:
        for _ in range(0 , s2 - s1):
            temp2 = temp2.next
    while temp1.next is not None:
        if temp1 == temp2:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next


def checkIntersection(sll1, sll2):
    tail1 = sll1.head
    size1 = 1
    while tail1.next is not None:
        size1 += 1
        tail1 = tail1.next

    tail2 = sll2.head
    size2 = 1
    while tail2.next is not None:
        size2 += 1
        tail2 = tail2.next
    if tail1 == tail2:
        pivot = findIntersectionNode(sll1, sll2, size1, size2)
        print("They intersect at:", pivot.data)
    else:
        print("They do not intersect!")


def createTestData():
    sll1 = singleLinkedList.LinkedList()
    testData1 = [1, -1, 4, 0, 67, -1, 34]
    # create input linked list
    for _ in testData1[::-1]:
        # O(1)
        sll1.insertStart(_)

    # select intersection point
    intersection = sll1.head
    for _ in range(0, 5):
        intersection = intersection.next

    sll2 = singleLinkedList.LinkedList()
    testData2 = [56, -91, 44, 7, 33]
    # create input linked list
    for _ in testData2[::-1]:
        # O(1)
        sll2.insertStart(_)

    # attach tail of sll2 to intersection point of sll1
    tail = sll2.head
    while tail.next is not None:
        tail = tail.next
    tail.next = intersection
    return sll1, sll2


sll1, sll2 = createTestData()
checkIntersection(sll1, sll2)
