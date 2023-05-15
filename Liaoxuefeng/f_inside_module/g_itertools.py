"""itertools
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"""
import itertools
import time

# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
# 1
# 2
# 3
# .....
print("-" * 15, "count()", "-" * 15)


def count_infinity(limit):
    naturals = itertools.count(1)
    for n in naturals:
        time.sleep(0.5)
        print(n)
        if n >= limit:
            break


count_infinity(3)

# cycle()会把传入的一个序列无限重复下去
print("-" * 15, "cycle()", "-" * 15)
cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
count_c = 0  # 定义c出现的次数, 如果超过2次就停止循环
for c in cs:
    time.sleep(0.5)
    print(c)
    if c == 'C':
        count_c += 1
    if count_c >= 2:
        break

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
print("-" * 15, "cycle()", "-" * 15)
ns = itertools.repeat('A', 3)
for n in ns:
    time.sleep(0.2)
    print(n)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
print("-" * 15, "takewhile()", "-" * 15)
naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, naturals)
print(type(ns))
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
print("-" * 15, "chain()", "-" * 15)
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
print("-" * 15, "groupby()", "-" * 15)
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 忽略大小写来使用groupby
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


# 可以使用这个公式来计算圆周率:
# pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 .....
# 定义一个函数来计算pi
def pi(n):
    sum = 0
    flag = True  # 判断正负号
    naturals = itertools.count(1, 2)  # 由1开始, 步长为2, 一次递增
    ns = itertools.takewhile(lambda x: x <= n, naturals)
    for x in ns:
        if flag:
            sum += 4 / x
            flag = False
        else:
            sum -= 4 / x
            flag = True

    return sum


print(pi(1000 * 1000 * 100))  # 3.1415926335902506
