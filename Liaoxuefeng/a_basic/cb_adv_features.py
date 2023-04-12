"""
四. 生成器generator
一边循环一边计算的机制
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
"""

g = (x * x for x in range(10))
# 可以使用next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# 也可以使用for循环进行迭代,因为generator也是可迭代对象
print(type(g))
for n in g:
    print(n)


# 生成斐波那契数列的函数
# 斐波那切数列: 这个数列从第3项开始，每一项都等于前两项之和。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        # 相当于 (a, b) = (b, a+b) 即
        # t = (b, a + b)
        # a = t[0]
        # b = t[1]
        n += 1  # 实际上python并不支持n++这样的写法, 因为变量类型并不确定
    return 'done'


"""
一个斐波那切数列的生成器
把上面的print(b)改为yield b 即变成一个生成器
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
这里，最难理解的就是generator函数和普通函数的执行流程不一样。
普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
需要注意的是 fib_generator(odd())
"""


def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'  # 这个生成器返回的字符串"done"并不是必须的，而是作为函数调用的时候可以返回一段字符串


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

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
