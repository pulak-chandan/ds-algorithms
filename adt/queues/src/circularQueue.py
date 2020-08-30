# Preferable
class CircularQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = [None] * maxSize
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        # modified
        return self.front == -1

    def isFull(self):
        # modified
        return (self.rear == (self.maxSize - 1) and self.front == 0) or (self.front - self.rear == 1)

    def enqueue(self, data):
        if not self.isFull():
            # circular condition
            if self.rear == (self.maxSize - 1):
                self.rear = 0

            elif self.isEmpty():
                self.front = self.rear = 0

            else:
                self.rear += 1

            self.items[self.rear] = data
        else:
            print("Queue Full!")

    def dequeue(self):
        if not self.isEmpty():
            temp = self.items[self.front]
            # reset queue if it is the only item
            if self.front == self.rear:
                self.front = self.rear = -1

            # circular condition
            elif self.front == (self.maxSize - 1):
                self.front = 0
            else:
                self.front += 1
            return temp

    def peek(self):
        if not self.isEmpty():
            return self.items[self.front]

    def display(self):
        if not self.isEmpty():
            if self.front <= self.rear:
                for _ in range(self.front, self.rear + 1):
                    print(self.items[_])
            else:
                for _ in range(self.front, self.maxSize):
                    print(self.items[_])
                for _ in range(0, self.rear + 1):
                    print(self.items[_])
        else:
            print("Empty queue!")


q = CircularQueue(3)
while True:
    x = int(input("enqueue --> 1, dequeue --> 2, peek --> 3, display --> 4:"))
    if x == 1:
        q.enqueue(input("Data:"))
    elif x == 2:
        print(q.dequeue(), "dequeued.")
    elif x == 3:
        print(q.peek())
    elif x == 4:
        q.display()
