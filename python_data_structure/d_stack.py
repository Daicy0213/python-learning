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

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(4)
s.push(3)
s.push(5)
# [4,3,5]
print(s.pop())  # 5, 栈内元素为[4,3]
print(s.top())  # 3
