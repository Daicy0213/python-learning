"""
用于测试时间复杂度的方法
关于python数据结构的性能最新消息详见: https://wiki.python.org/moin/TimeComplexity
以下为生成列表的四种方式
"""
import timeit


def for_add():
    l = []
    for i in range(1000):
        l = l + [i]


def for_append():
    l = []
    for i in range(1000):
        l.append(i)


def list_comprehensions():  # 列表生成式
    l = [i for i in range(1000)]


def list_range():
    l = list(range(1000))


num1 = 1000
num2 = 10000
Timer = timeit.Timer
t1 = Timer("for_add()", "from __main__ import for_add")
print("concat ", t1.timeit(number=num2), "milliseconds")
t2 = Timer("for_append()", "from __main__ import for_append")
print("append ", t2.timeit(number=num2), "milliseconds")
t3 = Timer("list_comprehensions()", "from __main__ import list_comprehensions")
print("comprehension ", t3.timeit(number=num2), "milliseconds")
t4 = Timer("list_range()", "from __main__ import list_range")
print("list range ", t4.timeit(number=num2), "milliseconds")

# number = 1000
# concat  0.5143874000059441 milliseconds
# append  0.01673040000605397 milliseconds
# comprehension  0.012511799985077232 milliseconds
# list range  0.003981799993198365 milliseconds

# number = 10000
# concat  5.005862899997737 milliseconds
# append  0.16860469998209737 milliseconds
# comprehension  0.1270710999961011 milliseconds
# list range  0.037034800014225766 milliseconds
