class QueueUsingList:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None
        temp = self.items[0]
        self.items = self.items[1:]
        return temp

    def peek(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None
        return self.items[0]


# Array like implementation, w/o using benefits of a List
# Problem: Once we store item in the last position, we cannot enqueue until and unless we dequeue all items.
class FixedSizeQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = [None] * maxSize
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == (self.maxSize - 1)

    def enqueue(self, data):
        if not self.isFull():
            self.rear += 1
            self.items[self.rear] = data
            if self.isEmpty():
                self.front += 1
        else:
            print("Queue Full!")

    def dequeue(self):
        if not self.isEmpty():
            temp = self.items[self.front]

            # reset queue if it's the last item in queue
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            return temp

    def peek(self):
        if not self.isEmpty():
            return self.items[self.front]


q = FixedSizeQueue(5)
while True:
    x = int(input("enqueue --> 1, dequeue --> 2, peek --> 3:"))
    if x == 1:
        q.enqueue(input("Data:"))
    elif x == 2:
        print(q.dequeue(), "dequeued.")
    elif x == 3:
        print(q.peek())



