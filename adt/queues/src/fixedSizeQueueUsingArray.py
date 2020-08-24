'''Array like implementation, w/o using benefits of a List
Problem: once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.
Solution: Circular Queue'''


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
            if self.isEmpty():
                self.front = self.rear = 0
            else:
                self.rear += 1

            self.items[self.rear] = data

        else:
            print("Queue Full!")

    def dequeue(self):
        if not self.isEmpty():
            temp = self.items[self.front]

            # reset queue if it's the only item in queue
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            return temp

    def peek(self):
        if not self.isEmpty():
            return self.items[self.front]