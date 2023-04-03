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


print("trim函数的执行结果:", trim('  abc  '), "\n")

"""
二. 迭代
"""
print("------------迭代------------")
L = [7, 1, 3, 9, 5]
print("字符串是否可以迭代", isinstance('abc', Iterable))
print("数字7的索引位置", L.index(7))


# 找到最小值和最大值
def find_min_and_max(l):
    if l:
        max = min = l[0]
        for a in l:
            if a < min:
                min = a
        for b in l:
            if b > max:
                max = b

        return min, max
    return None, None


print("L中的最大值和最小值为:", find_min_and_max(L))

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print()

"""
三. 列表生成式 List Comprehensions
用来创建list的生成式
"""
print("------------列表生成式 List Comprehensions------------")
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
# 原因是列表生成式构造为 [最终表达式 - 循环 - 筛选条件] 筛选条件即不能有else
print('打印10以内的所有偶数')
List = [x for x in range(1, 11) if x % 2 == 0]
print(List)

# 判断在前 必须加else
# 原因是列表生成式构造为 [最终表达式 - 条件分支表达式 - 循环] 表达式必须产生一个结果
List = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(List)


# 不能在最后的if加上else：
# 错误写法: [x for x in range(1, 11) if x % 2 == 0 else 0]


def lower_str_list(str_list):
    return [s.lower() for s in str_list if isinstance(s, str)]


# 将L1中的字符串全部变为小写并装入L2中
L1 = ['Hello', 'World', 18, 'Apple', None]
print(lower_str_list(L1))
