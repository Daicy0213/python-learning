"""
装饰器Decorator
本质上，decorator就是一个返回函数的高阶函数。
https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
"""
import functools
import time

print('---------装饰器---------')


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
print()
"""
我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
但是它们的__name__已经从原来的 'now' 变成了 'wrapper' , 这不符合装饰器的定义, 即只增强函数而不修改函数
Python内置的@functools.wraps 提供了对应的功能, 不需要编写wrapper.__name__ = func.__name__这样的代码
"""
print('-----------good wraps-----------')


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

print()
print("-----------metric-----------")


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
    print("Kobe is the MVP")


Kobe()
print('name: ', Kobe.__name__)
