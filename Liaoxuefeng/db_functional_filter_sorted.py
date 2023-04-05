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
