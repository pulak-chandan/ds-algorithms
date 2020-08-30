import datastructures.linkedLists.src.singleLinkedList as singleLinkedList


def sumOfListsForward():
    sum1 = sum2 = 0
    if not sll1.isEmpty():
        temp = sll1.head
        while temp is not None:
            sum1 = (sum1 * 10) + temp.data
            temp = temp.next
    if not sll2.isEmpty():
        temp = sll2.head
        while temp is not None:
            sum2 = (sum2 * 10) + temp.data
            temp = temp.next
    return sum1 + sum2


def sumOfListsRev():
    sum1 = sum2 = 0
    if not sll1.isEmpty():
        temp = sll1.head
        exp = 0
        while temp is not None:
            sum1 = sum1 + (pow(10, exp) * temp.data)
            exp += 1
            temp = temp.next
    if not sll2.isEmpty():
        temp = sll2.head
        exp = 0
        while temp is not None:
            sum2 = sum2 + (pow(10, exp) * temp.data)
            exp += 1
            temp = temp.next
    return sum1 + sum2


sll1 = singleLinkedList.LinkedList()
sll2 = singleLinkedList.LinkedList()
testData1 = [1, 9]
testData2 = [2, 4, 9]
'''
Output: 
91 + 942 = 1033
19 + 249 = 268
'''
# create input linked list
for _ in testData1[::-1]:
    # O(1)
    sll1.insertStart(_)

for _ in testData2[::-1]:
    # O(1)
    sll2.insertStart(_)

print(sumOfListsRev())
print(sumOfListsForward())
