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


print('---------闭包---------')
"""
1.闭包
如果不需要立刻求和，而是在后面的代码中，根据需要再计算，调用lazy_sum()时，返回的并不是求和结果，而是求和函数
调用函数f时，才真正计算求和的结果
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为"闭包（Closure）"
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


def outer_fn():
    i = 0

    def inner_fn():
        nonlocal i
        i = i + 1
        print(i)

    return inner_fn


f1 = outer_fn()
f2 = outer_fn()

f1()
f2()
f1()
f2()

print('---------闭包1---------')


# nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
def create_counter(i):
    def counter():
        nonlocal i

        i += 1

        return i

    return counter


counterA = create_counter(10)
counterB = create_counter(0)
print(counterA())  # 11
print(counterA())  # 12
print(counterB())  # 1
print(counterA())  # 13
print(counterB())  # 2
# 可以获得counterA的所有闭包的信息
print(counterA.__closure__)
