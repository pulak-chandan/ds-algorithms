import datastructures.linkedLists.src.singleLinkedList as singleLinkedList

'''
input:  10 -> 20 -> 30 -> 40 -> 50 -> -10 -> -20 -> -30 -> -40 -> -50
output: 10 -> -10 -> 20 -> -20 -> 30 -> -30 -> 40 -> -40 -> 50 -> -50
'''


def removeDup():
    if not sll.isEmpty():
        # set implements Hash Table, so best for look ups in O(1) on an average.But in worst case it can be O(N)
        seen = set()
        prev = None
        temp = sll.head
        while temp is not None:
            if temp.data in seen:
                sll.deleteNode(prev, temp)
            else:
                seen.add(temp.data)
                prev = temp
            temp = temp.next


sll = singleLinkedList.LinkedList()
testData = [1, -1, 4, 0, 67, -1, 34, 67, -1, 22, 22, 100, 1, 98, 4, 67]
# create input linked list
'''
for _ in testData:
    # O(N)
    sll.insertEnd(_)
'''
for _ in testData[::-1]:
    # O(1)
    sll.insertStart(_)

removeDup()
print("Output:")
sll.traverse()
