"""
函数式编程
"""
import time, functools

"""
二.返回函数
"""

"""
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
"""


# 一个可变参数的求和可以如下定义
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print('##### 闭包 START #####')
"""
1.闭包
如果不需要立刻求和，而是在后面的代码中，根据需要再计算，调用lazy_sum()时，返回的并不是求和结果，而是求和函数
调用函数f时，才真正计算求和的结果
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）
"""


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3)
print(f())


def outerFn():
    i = 0

    def innerFn():
        nonlocal i
        i = i + 1
        print(i)

    return innerFn


f1 = outerFn()
f2 = outerFn()

f1()
f2()
f1()
f2()


# nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
def createCounter():
    i = 0

    def counter():
        nonlocal i

        i += 1

        return i

    return counter


print('##### 闭包 END #####')
"""
2.匿名函数
在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
"""
print('##### 匿名函数 START #####')
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

"""
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
"""

f = lambda x: x * x
print(f(5))
print('##### 匿名函数 END #####')
"""
装饰器Decorator
本质上，decorator就是一个返回函数的高阶函数。
https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
"""
print('##### 装饰器 START #####')


# 定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处


@log
def now():
    print(time.asctime(time.localtime(time.time())))


# 相当于now = log(now)
now()
print('name: ', now.__name__)

"""
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
"""


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print(time.asctime(time.localtime(time.time())))


# 相当于now = log('execute')(now)
now()
print('name: ', now.__name__)

"""
我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
但是它们的__name__已经从原来的'now'变成了'wrapper', 这不符合装饰器的定义, 即只增强函数而不修改函数
Python内置的@functools.wraps 提供了对应的功能, 不需要编写wrapper.__name__ = func.__name__这样的代码
"""


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print(time.asctime(time.localtime(time.time())))


now()
print('name: ', now.__name__)

"""
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
"""


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        re = fn(*args, **kw)  # 执行函数
        cost = time.time() - start
        print('%s executed in %s ms' % (fn.__name__, cost))
        return re

    return wrapper


@metric
def Kobe():
    print("MVP")


Kobe()
print('name: ', Kobe.__name__)
print('##### 装饰器 END #####')

"""
偏函数
Python的#functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
"""
print('##### 偏函数 START #####')
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print(int('12345', base=8))  # 将八进制的12345转换为十进制
print(int('F32CD', 16))  # 将十六进制的F32CD转换为十进制

# functools.partial就是帮助我们创建一个偏函数, 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
# 二进制转换的函数
int2 = functools.partial(int, base=2)
print(int2('10000'))

# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# int2函数中, 相当于kw = { 'base': 2 }

print('##### 偏函数 END #####')
