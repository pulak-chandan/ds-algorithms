import datastructures.linkedLists.src.singleLinkedList as singleLinkedList


class Stack:
    def __init__(self):
        self.items = singleLinkedList.LinkedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def push(self, data):
        self.items.insertStart(data)

    def pop(self):
        if not self.isEmpty():
            x = self.items.head.data
            self.items.deleteStart()
            return x

    def peek(self):
        if not self.isEmpty():
            return self.items.head.data


'''
stk = Stack()
while True:
    x = int(input("0: push, 1: pop, 2: peek:"))
    if x == 0:
        stk.push(int(input("Data:")))
    elif x == 1:
        print(stk.pop())
    elif x == 2:
        print(stk.peek())
'''

