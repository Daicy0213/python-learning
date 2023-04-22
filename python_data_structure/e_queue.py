class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enq(self, item):
        self.items.insert(0, item)

    def deq(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()
