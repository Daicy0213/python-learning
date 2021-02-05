"""
函数式编程
"""

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


def createCounter():
    i = 0

    def counter():
        nonlocal i

        i += 1

        return i

    return counter


"""
2.匿名函数
在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
"""
