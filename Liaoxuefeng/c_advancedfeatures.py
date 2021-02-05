"""
高级特性
"""
import collections.abc
import os
from collections.abc import Iterable

"""
一. 切片Slice
"""

# 1. range函数
L = list(range(20))
print(L)

# 2. 字符串也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
# 'ABCDEFG'[:3] ===> for(i=0;i<3;i++)
print('ABCDEFG'[:3])  # 打印从0至3
# 'ABCDEFG'[::2] ===> for(i=0;i<str.length;i=i+2)
print('ABCDEFG'[::2])  # 每间隔一个打印


# 3. 使用切片实现Java中的String.trim()
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


print("trim函数的执行结果:", trim('  abc  '))

"""
二. 迭代
"""

L = [7, 1, 3, 9, 5]
print("字符串是否可以迭代", isinstance('abc', Iterable))
print("数字7的索引位置", L.index(7))


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

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

"""
三. 列表生成式 List Comprehensions
用来创建list的生成式
"""

print("生成1-10的平方:")
List = [x * x for x in range(1, 11)]  # 生成1-10的平方
print(List)

print("笛卡尔积")
List = [m + n for m in 'ABC' for n in 'XYZ']  # 笛卡尔积
print(List)

print("列出当前目录下的所有文件和目录名")
List = [d for d in os.listdir('.')]  # 列出当前目录下的所有文件和目录名
print(List)

print('生成当前目录下的所有文件的编号与文件名对应的dict')
listdir = os.listdir('.')
dicta = {}
i = 0
for d in listdir:
    dicta[i] = d
    i = i + 1
print(dicta)

# 使用items()函数遍历,同时迭代key和value
for k, v in dicta.items():
    print(k, '=', v)

# 使用列表生成器中的if...else...
# 判断在后 不加else
print('打印10以内的所有偶数')
List = [x for x in range(1, 11) if x % 2 == 0]
print(List)

# 判断在前 必须加else
List = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(List)
# 不能在最后的if加上else：
# 错误写法: [x for x in range(1, 11) if x % 2 == 0 else 0]

# 将L1中的字符串全部变为小写并装入L2中
L1 = ['Hello', 'World', 18, 'Apple', None]


def lowerStrList(str_list):
    return [s.lower() for s in str_list if isinstance(s, str)]


print(lowerStrList(L1))

"""
四. 生成器generator
一边循环一边计算的机制
"""


# 生成斐波那契数列的函数
# 斐波那切数列: 这个数列从第3项开始，每一项都等于前两项之和。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        # 相当于
        # t = (b, a + b)
        # a = t[0]
        # b = t[1]
        n = n + 1
    return 'done'


# 一个斐波那切数列的生成器
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 使用循环迭代斐波那切数列的生成器
List = []
for i in fib_generator(10):
    List.append(i)
print(List)

"""
五. 迭代器
可以直接作用于for循环的对象统称为可迭代对象：Iterable
可以使用isinstance()判断一个对象是否是Iterable对象

而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)

Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，
只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
"""
