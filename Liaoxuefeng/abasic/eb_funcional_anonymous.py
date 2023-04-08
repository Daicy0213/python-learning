"""
2.匿名函数
在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
"""
print('---------匿名函数---------')
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

"""
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
"""

f = lambda x: x * x
print(f(5))
print()

# 如果返回的是lambda函数
print("---------返回匿名函数1---------")


def build_xy(x, y):
    return lambda: x * x + y * y


bxy = build_xy(1, 2)
print(bxy())

print("---------返回匿名函数2---------")


def build():
    return lambda x, y: x * x + y * y


b = build()(1, 2)
print(b)

print("---------返回匿名函数3---------")


def outer_func(person="Jerry"):
    return lambda location="": person + " in the " + location


Lead = outer_func("Tom")("China")

print(Lead)
print("---------返回匿名函数4---------")


def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)
my_tripler = myfunc(3)

print(my_doubler(11))
print(my_tripler(11))
