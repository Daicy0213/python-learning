"""
栈
自身维护一个list, 仅在出入口做限制
"""


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        result = '['
        for i in self.items:
            result += str(i) + ', '
        return result[:-2] + ']'

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(4)
s.push(3)
s.push(5)

print(s.pop())
print(s.peek())
