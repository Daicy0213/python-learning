"""
函数式编程
越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。
函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量。
因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
"""
from functools import reduce

"""
一.高阶函数(high-order function)
变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
"""


# 求两个数的绝对值之和
def add(x, y, fun=abs):
    return fun(x) + fun(y)


print("绝对数求和:", add(1, -1))
print()

"""
map
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现
"""

print("-" * 10 + "map/reduce" + "_" * 10)


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])
print("map求平方:", list(r))


# 如果map(function，iterable...)中的function需要多个参数, 则可以传入多个数组
def build(x, y):
    return x * x + y * y


print("求多组数字的平方和:", list(map(build, [1, 2, 3], [1, 2, 3])))

"""
reduce
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
使用等式可以理解为: reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
"""


def fn(x, y):
    return x * 10 + y


print("将数组转化为数字:", reduce(fn, [1, 3, 5, 7, 9]))

# 可以将结果在字符串与数字之间转换, 使用lambda函数进一步简化
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print("将字符串转化为数字:", str2int("13579"))


# 将名字标准化
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize, L1)))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(li):
    return reduce(lambda x, y: x * y, li)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    a, b = s.split('.')
    return reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), a)) \
           + reduce(lambda x, y: x * 0.1 + y, map(lambda x: int(x), b[::-1])) * 0.1


print(str2float('123.456'))
