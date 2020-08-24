class Queue:
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