class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# SingleLinkedList class wraps the Node class. Has a relationship (LinkedList has a Node)
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    # O(1)
    def insertStart(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    # O(N)
    def insertEnd(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        self.size += 1

    # O(N)
    def insertAfter(self, data, pivot):
        if not self.isEmpty():
            temp = self.head
            while temp.data != pivot:
                if temp.next is None:
                    print("Pivot element no found!")
                    return
                temp = temp.next
            newNode = Node(data)
            newNode.next = temp.next
            temp.next = newNode
            self.size += 1

    # O(1) -- Better, just maintain extra attribute called size
    def listSize(self):
        return self.size

    # O(N) - Not recommended
    def sizeOfList(self):
        if self.isEmpty():
            return 0
        else:
            temp = self.head
            length = 1
            while temp.next is not None:
                temp = temp.next
                length += 1
            return length

    def deleteStart(self):
        if self.isEmpty():
            print("List is empty!")
        else:
            self.head = self.head.next
            self.size -= 1

    # We can leverage size attribute of the list as well.
    def deleteEnd(self):
        if self.isEmpty():
            print("List is empty!")
        else:
            temp = self.head
            if temp.next is not None:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
            else:
                self.head = None
            self.size -= 1

    # w/o using prev pointer
    def deleteData(self, data):
        if not self.isEmpty():
            if self.head.data == data:
                self.head = self.head.next
                self.size -= 1
            else:
                temp = self.head
                while temp.next is not None:
                    if temp.next.data == data:
                        temp.next = temp.next.next
                        self.size -= 1
                        return
                    temp = temp.next
                print("Element not found!")
        else:
            print("List is empty")

    def deleteNode(self, prev, node):
        if not self.isEmpty():
            # remove head node
            if node == self.head:
                self.head = self.head.next
            else:
                prev.next = node.next

    def traverse(self):
        if not self.isEmpty():
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

'''
l = LinkedList()
while True:
    x = int(input("0: insertEnd, 1: insertStart, 2: insertAfter, 3: listSize, 4:display, 5: deleteData:"))
    if x == 0:
        l.insertEnd(input("Data:"))
    elif x == 1:
        l.insertStart(input("Data:"))
    elif x == 2:
        l.insertAfter(input("Data:"), input("Insert after:"))
    elif x == 3:
        print(l.listSize(), l.sizeOfList())
    elif x == 4:
        l.traverse()
    elif x == 5:
        l.deleteData(input("Data:"))
'''
