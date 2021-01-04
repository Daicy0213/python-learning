""" 高级特性 """
import collections.abc
from collections.abc import Iterable

"""一. 切片Slice"""
# 1. range函数
L = list(range(20))
print(L)

# 2. 字符串也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])


# 3. 使用切片实现Java中的String.trim()
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


print("trim函数的执行结果:", trim('  abc  '))

"""二. 迭代"""

L = [7, 1, 3, 9, 5]
print("字符串是否可以迭代", isinstance('abc', Iterable))


# 找到最小值和最大值
def findMinAndMax(list):
    if list:
        max = min = list[0]
        for a in list:
            if a < min:
                min = a
        for b in list:
            if b > max:
                max = b

        return (min, max)
    return (None, None)


print("L中的最大值和最小值为:", findMinAndMax(L))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

print(L.index())
