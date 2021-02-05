"""
函数式编程
"""
from functools import reduce

"""
一.高阶函数(high-order function)
变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
"""


# 求两个数的绝对值之和
def add(x, y, fun=abs):
    return fun(x) + fun(y)


print(add(1, -1))

"""
map
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现
"""


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])
print(list(r))

"""
reduce
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
使用等式可以理解为: reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
"""


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

"""
filter
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素
然后根据返回值是True还是False决定保留还是丢弃该元素。
"""


# 一个过滤掉所有偶数的过滤器
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 删掉序列中的空字符串的过滤器
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

"""
用filter求素数
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 5, 7, 9, 11, 13, 15, 17, 19, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 7, 11, 13, 17, 19, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 11, 13, 17, 19, ...
不断筛下去，就可以得到所有的素数。
"""


# 构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数
def primes(Max):
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        if n > Max:
            break
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印100以内的素数:
print(list(primes(100)))

"""
排序算法
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
"""

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[1]


def by_name(t):
    return t[0]


print(sorted(L, key=by_score))
print(sorted(L, key=by_name))
