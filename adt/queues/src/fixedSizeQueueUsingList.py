class FixedSizeQueueUsingList:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.maxSize

    def enqueue(self, data):
        if self.isFull():
            print("Queue Full!")
        else:
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