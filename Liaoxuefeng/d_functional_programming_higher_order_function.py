""" 函数式编程 """
from functools import reduce

"""一.高阶函数(high-order function)
变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。"""


# 求两个数的绝对值之和
def add(x, y, fun=abs):
    return fun(x) + fun(y)


print(add(1, -1))

"""map
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现"""


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])
print(list(r))

"""reduce
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
使用等式可以理解为: reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场"""


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))

# 可以将结果在字符串与数字之间转换, 使用lambda函数进一步简化
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int("13579"))


# 将名字标准化
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize, L1)))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    a, b = s.split('.')
    return reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), a)) + reduce(lambda x, y: x * 0.1 + y,
                                                                              map(lambda x: int(x), b[::-1]))


print(str2float('123.456'))

"""filter
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素
然后根据返回值是True还是False决定保留还是丢弃该元素。
"""
